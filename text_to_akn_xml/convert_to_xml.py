from lxml.builder import ElementMaker
from lxml import etree as ET
from cobalt import Debate
from antlr4 import *
from tika import parser
from datetime import datetime as dt
import numpy as np
from collections import defaultdict
import re
import os
from bs4 import BeautifulSoup

import sys
sys.path.append('../antlr4_grammar')
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser

E = ElementMaker(nsmap={None: 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'},
                 namespace='http://docs.oasis-open.org/legaldocml/ns/akn/3.0')

starttime = dt.now()
record_date = "0000-00-00"
record_period = "00"
record_session = "00"
record_sitting = "00"

greek_to_english = {
    'α': 'a',
    'β': 'b',
    'γ': 'g',
    'δ': 'd',
    'ε': 'e',
    'ζ': 'z',
    'η': 'i',
    'θ': 'th',
    'ι': 'i',
    'κ': 'k',
    'λ': 'l',
    'μ': 'm',
    'ν': 'n',
    'ξ': 'x',
    'ο': 'o',
    'π': 'p',
    'ρ': 'r',
    'σ': 's',
    'ς': 's',
    'τ': 't',
    'υ': 'u',
    'φ': 'f',
    'χ': 'x',
    'ψ': 'ps',
    'ω': 'o',
}


def convert_greek_to_english(whole_phrase):
    words = whole_phrase.split()
    converted_words = []
    for word in words:
        word = word.lower()
        word = word.translate(str.maketrans(
            'άέόώήίϊΐiύϋΰ', 'αεοωηιιιιυυυ'))  # remove accents
        converted_word = ''
        for char in word:
            if char in greek_to_english:
                converted_word += greek_to_english[char]
            else:
                converted_word += char
        converted_words.append(converted_word)
    return '_'.join(converted_words)


def create_debateSection_akn(name="main_debate_section"):
    debateSection = (
        E.debateSection(name=name))  # create an Element called "debateSection"
    return debateSection


def create_scene_akn(xeir_sxolio):
    return E.scene(xeir_sxolio)


def create_speeches_akn(speaker, speeches, num):
    date_ = get_date(record_date).strftime('%Y-%m-%d')
    speaker_englishVersion = convert_greek_to_english(speaker)
    speech_ = speeches.split("\n")
    speech_.pop()
    paragraphs = [E.p(speech_[i].strip())
                  for i in range(len(speech_)) if speech_[i] != '']
    speech = E.speech(
        ET.XML(f"<from>{str(speaker)}</from>"),
        *paragraphs, by=f"{speaker_englishVersion}", eId=f'debate_{date_}_speech_{num}'
    )
    return speech


def create_preamble_akn(preamble_text, name="preamble"):
    preamble = E.p(preamble_text.strip())
    debateSection = (
        E.debateSection(name=name))
    debateSection.append(preamble)
    return debateSection


def create_toc_akn(tree):
    tree_toc = tree.table_of_contents()
    if tree_toc:
        tocs = []

        def get_text_or_none(child):
            result = [get_text_or_none(sub_child) if isinstance(sub_child, list) else (
                sub_child.getText() if sub_child is not None else None) for sub_child in child]
            if isinstance(child, list):
                return ' '.join(str(e) for e in result if e is not None)
            else:
                # Extract parliament details
                return result.getText() if result is not None else None
        all_tocs = [get_text_or_none(tree_toc.PINAKAS_PERIEXOMENON()),
                    get_text_or_none(tree_toc.anatheoritiki_bouli()),
                    get_text_or_none(tree_toc.dimokratia()),
                    get_text_or_none(tree_toc.ergasies()),
                    get_text_or_none(tree_toc.period_detail()),
                    get_text_or_none(tree_toc.sunodos()),
                    get_text_or_none(tree_toc.sunedriasi()),
                    get_text_or_none(tree_toc.date())]
        tocs.extend(
            item for item in all_tocs if item is not None)
        if tocs:
            parl_proceedings = E.container(name="first_toc")
            for item in tocs:
                if item != '':
                    parl_proceedings.append(E.p(item))
            return parl_proceedings


def create_themata_preface_akn(tree):
    tree_subjects = tree.subjects()
    if tree_subjects:
        themata_section = E.container(name="subjects")
        all_subjects = []
        for section in tree_subjects.sectionContent():
            if section.sbcategory() and section.sbcategory().SUBJECT_BASIC_CATEGORY():
                categ_name = E.p(
                    section.sbcategory().SUBJECT_BASIC_CATEGORY().getText())
                all_subjects.append(categ_name)
            for sub in section.subject():
                subject_text = sub.SUBJECT_().getText()
                subject_text = E.p(subject_text)
                all_subjects.append(subject_text)
        themata_section.extend(all_subjects)
        return themata_section


def create_proedreuontes_preface_akn(tree):
    tree_proedreuontes = tree.proedreuontes()
    if tree_proedreuontes:
        proedreuontes_section = E.container(name="proedreuontes")
        all_proedreuontes = []
        for proedreuontes in tree_proedreuontes:
            if (proedreuontes.PROEDREUONTES()):
                proed = E.p(
                    proedreuontes.PROEDREUONTES().getText())
                all_proedreuontes.append(proed)
            for proedreuontes_name in proedreuontes.proedreuontes_name():
                proedreuon_name = proedreuontes_name.NAME().getText()
                proedreuon_name = proedreuon_name.replace(" , σελ.", "")
                proedreuon_name_ = E.p(proedreuon_name)
                all_proedreuontes.append(proedreuon_name_)
        proedreuontes_section.extend(all_proedreuontes)
        return proedreuontes_section


def create_speakers_preface_akn(tree):
    tree_speakers = tree.speakers()
    if tree_speakers:
        speakers_section = E.container(name="speakers")
        all_speakers = []
        for speakers in tree_speakers.speaker_detail():
            if (speakers.SPEAKER_CATEG_DETAIL()):
                categ_name = E.p(
                    speakers.SPEAKER_CATEG_DETAIL().getText())
                all_speakers.append(categ_name)
            for speaker in speakers.speakers_name():
                speaker_name = speaker.NAME().getText()
                speaker_name = speaker_name.replace(" , σελ.", "")
                speaker_name_ = E.p(speaker_name)
                all_speakers.append(speaker_name_)
        speakers_section.extend(all_speakers)
        return speakers_section


def create_parl_proceedings_akn(tree):
    tree_parlDetails = tree.parliament_proceedings()
    if tree_parlDetails:
        tree_parlDetails = tree_parlDetails.parliament_detail()
        all_parlDetails = []
        # Extract parliament details
        parliament_details = [
            tree.parliament_proceedings().PRAKTIKA_BOULIS().getText(
            ) if tree.parliament_proceedings().PRAKTIKA_BOULIS() is not None else None,
            tree_parlDetails.anatheoritiki_bouli().getText(
            ) if tree_parlDetails.anatheoritiki_bouli() is not None else None,
            tree_parlDetails.period_detail().getText(
            ) if tree_parlDetails.period_detail() is not None else None,
            tree_parlDetails.dimokratia().getText(
            ) if tree_parlDetails.dimokratia() is not None else None,
            tree_parlDetails.sunodos().getText(
            ) if tree_parlDetails.sunodos() is not None else None,
            [ergasies.getText() for ergasies in tree_parlDetails.ergasies()
             ] if tree_parlDetails.ergasies() is not None else None,
            tree_parlDetails.sunedriasi().getText(
            ) if tree_parlDetails.sunedriasi() is not None else None,
            tree_parlDetails.date().getText() if tree_parlDetails.date() is not None else None
        ]

        all_parlDetails.extend(
            item for item in parliament_details if item is not None)
        if all_parlDetails:
            parl_proceedings = E.container(name="parliament_details")
            for item in all_parlDetails:
                if isinstance(item, list):
                    parl_proceedings.extend([E.p(subitem) for subitem in item])
                else:
                    parl_proceedings.append(E.p(item))
            return parl_proceedings


def create_meta_references_akn(type, name):
    name_ = convert_greek_to_english(name)
    if type == "TLCPerson":
        meta_reference = E.TLCPerson(
            eId=name_, href="/ontology/person/akn/parliament/"+str(name_), showAs=name)
    elif type == "TLCRole":
        meta_reference = E.TLCRole(
            eId=name_, href="/ontology/person/akn/parliament/"+str(name_), showAs=name)
    elif type == "TLCOrganization":
        meta_reference = E.TLCOrganization(
            eId=name_, href="/ontology/organization/akn/parliament/"+str(name_), showAs=name)
    return meta_reference


def create_preface_akn(debate, tree):
    preface_ = E.preface()
    toc_ = create_toc_akn(tree)
    themata_ = create_themata_preface_akn(tree)
    proedreuontes_ = create_proedreuontes_preface_akn(tree)
    speakers_ = create_speakers_preface_akn(tree)
    parl_proceedings_ = create_parl_proceedings_akn(tree)
    if not toc_ == None:
        preface_.append(toc_)
    if not themata_ == None:
        preface_.append(themata_)
    if not proedreuontes_ == None:
        preface_.append(proedreuontes_)
    if not speakers_ == None:
        preface_.append(speakers_)
    if not parl_proceedings_ == None:
        preface_.append(parl_proceedings_)
    debate.meta.addnext(preface_)
    return


def edit_meta_debate_akn(current_record_date):
    date_ = current_record_date.strftime('%Y-%m-%d')
    d.expression_date = str(date_)
    d.manifestation_date = str(date_)
    d.manifestation_format = "xml"
    d.frbr_uri = "/akn/gr/debate/"+str(date_)+"/1/"
    d.frbr_uri.work_componenent = ""
    d.language = "gr"
    d.title = "ΠΡΑΚΤΙΚΑ ΒΟΥΛΗΣ " + str(date_)


# Cleaning and formatting speakers data
def text_formatting(text):
    text = re.sub("[():'’`΄‘]", ' ', text)
    text = re.sub('\t+', ' ', text)  # replace one or more tabs with one space
    text = text.lstrip()  # remove leading spaces
    text = text.rstrip()  # remove trailing spaces
    # replace more than one spaces with one space
    text = re.sub('\s\s+', ' ', text)
    text = re.sub('\s*(-|–)\s*', '-', text)  # fix dashes
    # text = text.lower()
    # text = text.translate(str.maketrans('άέόώήίϊΐiύϋΰ','αεοωηιιιιυυυ')) #remove accents
    # text = text.translate(str.maketrans('akebyolruxtvhmnz','ακεβυολρυχτνημνζ')) #convert english chars to greek
    return text


def speaker_name_corrections(name):
    if 'γενηματα' in name:
        name = name.replace('γενηματα', 'γεννηματα')
    if 'βαρουφακης' in name:
        name = name.replace('γιαννης', 'γιανης')
    if 'ζουραρις' in name:
        name = name.replace('ζουραρις', 'ζουραρης')
    return name


# For example ΦΩΤΕΙΝΗ (ΦΩΦΗ ΓΕΝΝΗΜΑΤΑ (Πρόεδρος της Δημοκρατικής Συμπαράταξης ΠΑΣΟΚ - ΔΗΜΑΡ):,2017
def separate_nickname_incomplete_parenthesis(speaker, speaker_nickname):
    lefts = 0
    rights = 0
    if left_parenthesis_regex.search(speaker):
        lefts = len(re.findall(left_parenthesis_regex, speaker))
    if right_parenthesis_regex.search(speaker):
        rights = len(re.findall(right_parenthesis_regex, speaker))
    if (lefts-rights) > 0:
        if incomplete_nickname_parenthesis.search(speaker):
            # Keep separately the nickname of the speaker
            speaker_nickname = (
                incomplete_nickname_parenthesis.search(speaker)).group()
            speaker_nickname = text_formatting(speaker_nickname)
            speaker = re.sub(incomplete_nickname_parenthesis,
                             '', speaker)  # remove nickname
    return speaker, speaker_nickname


# Keep separately the nickname of the speaker
def separate_nickname(speaker):
    speaker_nickname = (caps_nickname_in_parenthesis.search(speaker)).group()
    speaker_nickname = text_formatting(speaker_nickname)
    speaker = re.sub(caps_nickname_in_parenthesis,
                     '', speaker)  # remove nickname
    return speaker, speaker_nickname


# Keep separately the explanatory parenthesis text of the speaker
def separate_explanatory_parenthesis(speaker):
    speaker_info = (text_in_parenthesis.search(speaker)).group()
    # remove (text in parenthesis)
    speaker = re.sub(text_in_parenthesis, '', speaker)
    return speaker, speaker_info


def format_speaker_info(speaker_info):
    speaker_info = text_formatting(speaker_info)
    speaker_info = speaker_info.replace('υφυπ.', ' υφυπουργος ')
    speaker_info = speaker_info.replace('υπ.', ' υπουργος ')
    speaker_info = speaker_info.replace('&', ' και ')
    # replace more than one spaces with one space
    speaker_info = re.sub('\s\s+', ' ', speaker_info)
    speaker_info = speaker_info.lstrip()  # remove leading spaces
    speaker_info = speaker_info.rstrip()  # remove trailing spaces
    return speaker_info


def month_to_number(month):

    months = {'ιανουαριου': '1', 'φεβρουαριου': '2', 'μαρτιου': '3',
              'απριλιου': '4', 'μαιου': '5', 'ιουνιου': '6', 'ιουλιου': '7',
              'αυγουστου': '8', 'σεπτεμβριου': '9', 'οκτωβριου': '10',
              'νοεμβριου': '11', 'δεκεμβριου': '12'}

    return months[month]


def get_date(date):
    # if megali ebdomada, delete M.
    date = date.replace("Μ.", "").strip()
    year = date.split()[3]
    day = date.split()[1]
    month = date.split()[2]
    # Fix some cases
    day = re.findall(r'\d+', day)[0]
    year = re.findall(r'\d+', year)[0]
    if month == "Μα|ου" or month == "Mα|ου":
        month = "Μαίου"
    if year == "2202":
        year = "2002"
    month = month.translate(str.maketrans(
        'άΆέΈόΌώΏήΉίΊϊΐύΎϋΰ', 'αΑεΕοΟωΩηΗιΙιιυΥυυ')).lower()  # remove accents&lower
    month = month_to_number(month)
    date = dt.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
    return date


def set_record_values(tree):
    tree_parlDetails = tree.parliament_proceedings()
    tree_toc = tree.table_of_contents()
    if tree_parlDetails:
        tree_parlDetails = tree_parlDetails.parliament_detail()
        # Extract parliament details
        period_detail = tree_parlDetails.period_detail().getText(
        ) if tree_parlDetails.period_detail() is not None else None
        sunodos = tree_parlDetails.sunodos().getText(
        ) if tree_parlDetails.sunodos() is not None else None
        sunedriasi = tree_parlDetails.sunedriasi().getText(
        ) if tree_parlDetails.sunedriasi() is not None else None
        date = tree_parlDetails.date().getText(
        ) if tree_parlDetails.date() is not None else None
    elif tree_toc:
        def get_text_or_none(child):
            result = [get_text_or_none(sub_child) if isinstance(sub_child, list) else (
                sub_child.getText() if sub_child is not None else None) for sub_child in child]
            if isinstance(child, list):
                return ' '.join(str(e) for e in result if e is not None)
            else:
                # Extract parliament details
                return result.getText() if result is not None else None
        period_detail = get_text_or_none(tree_toc.period_detail())
        sunodos = get_text_or_none(tree_toc.sunodos())
        sunedriasi = get_text_or_none(tree_toc.sunedriasi())
        date = get_text_or_none(tree_toc.date())

    global record_date, record_period, record_session, record_sitting
    record_date = date
    record_period = period_detail
    record_session = sunodos
    record_sitting = sunedriasi


def format_speaker_information(speaker_, speaker_nickname_, flagMetaReferences=False):
    speaker_info = ""
    if flagMetaReferences:
        if proedr_regex.search(speaker_):
            segments = speaker_.split('(')
            speaker_ = ''.join(segments[1:])
    speaker, speaker_nickname = separate_nickname_incomplete_parenthesis(
        speaker_, speaker_nickname_)

    if caps_nickname_in_parenthesis.search(speaker):
        speaker, speaker_nickname = separate_nickname(speaker)

    if text_in_parenthesis.search(speaker):
        speaker, speaker_info = separate_explanatory_parenthesis(
            speaker)
        speaker_info = format_speaker_info(speaker_info)

    speaker_name = text_formatting(speaker)
    speaker_name = speaker_name_corrections(speaker_name)
    return (speaker_name, speaker_info, speaker_nickname)


datapath = "C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/files/all_files/"
parsed1 = parser.from_file(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/files/all_files/297.docx', xmlContent=True)

# print(parsed["metadata"]["dcterms:created"])
# print(parsed1["content"])
# f1_path = args.outpath
# f2_path = args.outpath2


filenames = sorted([f for f in os.listdir(datapath) if not f.startswith('.')])
print(filenames)
filename_freqs = defaultdict(int)

record_counter = 0

# REGULAR EXPRESSIONS
# ------------------------------------------
speaker_regex = re.compile(
    r"((\s*[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)*\s*(\(.*?\))?\s*\:)")
caps_nickname_in_parenthesis = re.compile(r"(\([Α-ΩΆ-ΏΪΫΪ́Ϋ́]+\))+")  # (ΠΑΝΟΣ)
lower_nickname_in_parenthesis = re.compile(r"(\([α-ω]{2,}\))")  # (πανος)
text_in_parenthesis = re.compile(r"(\(.*?\)){1}")  # (Υπουργός Εσωτερικών)

# Regex for both proedros or proedreuon
proedr_regex = re.compile(
    r"((((Π+Ρ(Ο|Ό)+(Ε|Έ))|(Ρ(Ο|Ό)+(Ε|Έ)Δ)|(ΠΡ(Ε|Έ)(Ο|Ό))|(ΠΡ(Ο|Ό)Δ)|(Η ΠΡ(Ο|Ό)(Ε|Έ)ΔΡ)|(ΠΡ(Ε|Έ)Δ))|(ΠΡΟΣΩΡΙΝΗ ΠΡΟΕΔΡΟΣ)|(ΠΡΟΣΩΡΙΝΟΣ ΠΡΟΕΔΡΟΣ)))")

# Regex for proedros only
proedros_regex = re.compile(r"ΠΡ((Ο|Ό|(ΟΟ))(Ε|Έ)|((ΕΟ)|(ΈΟ)|(ΕΌ)|(ΈΌ)))ΔΡΟΣ")
proedreuon_first_speaker = re.compile(
    r"((\s*[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)(\s+\(([Α-ΩΆ-Ώα-ωά-ώϊϋΐΰΪΫΪ́Ϋ́-]\s*)+\))?\s*\:)$")
general_member_regex = re.compile(
    r"((Β(Ο|Ό)(Υ|Ύ)(Ε|Έ)Λ)|(Β(Ο|Ό)(Υ|Ύ)Λ(Ε|Έ)(Υ|Ύ)?Τ[^(Α|Ά)]))")
left_parenthesis_regex = re.compile(r"\(")
right_parenthesis_regex = re.compile(r"\)")
incomplete_nickname_parenthesis = re.compile(r"\([Α-ΩΆ-ΏΪΫΪ́]{3,}\s")
sitting_terminated_regex = re.compile(r"λ(υ|ύ)εται\s+η\s+συνεδρ(ι|ί)αση")
comments_regex = re.compile(r"\(.*?\)[^:]{1}")
comment_sto_simio_auto = re.compile(
    r"(\(\s*(Σ|σ)το σημε(ί|ι)ο αυτ(ό|ο).*?\)).*\n*")
xeirokrotima = re.compile(r"\((χ|Χ)ειροκροτ(ή|η)ματα\s*.*?\)\n*")
allagi_selidas = re.compile(r"\(?ΑΛΛΑΓ(Η|Ή)\s*ΣΕΛ(Ι|Ί)ΔΑΣ\s*[Α-Ω]*\)")
starting_regex = re.compile(
    r"(Π\s*Ρ\s*Α\s*Κ\s*Τ\s*Ι\s*Κ\s*(Α|A)\s*(Τ\s*Η\s*Σ)?\s*Β\s*Ο\s*Υ\s*Λ\s*Η\s*Σ)\s*(.+)('|΄|`|’)\s*ΠΕΡΙΟΔΟΣ\s*\(?((ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)|(ΠΡΟΕΔΡΕΥ?Ο?ΜΕΝΗΣ? ΔΗΜ?ΟΚΡΑΤΙΑΣ))\)?\s*(Σ\s*Υ\s*Ν\s*Ο\s*Δ\s*Ο\s*Σ)?\s*(.+)('|΄|`|’)\s+(.*)\s*(Σ\s*Υ\s*Ν\s*Ε\s*Δ\s*Ρ\s*Ι\s*Α\s*Σ\s*Η|ΣΥΕΝΔΡΙΑ|Συνεδρίαση|ΣΥΕΝΔΡΙΑΣΗ)\s*(([Α-Ω]*)(΄|'|`|’)?)\s*([\u0386-\u03CE]+\s*,? \s*\d{1,2} \n*[\u0386-\u03CE]+\s*\d{4})")
preamble_regex = re.compile(r"(Αθήνα.*)")
ilektroniki_katametrisi_regex = re.compile(
    r"(\([Α-Ωα-ω\s]*ΗΛΕΚΤΡΟΝΙΚΗ\s*ΚΑΤΑ[Α-Ωα-ω]*\))")

# selida_num_regex = re.compile(r"\(?ΣΕΛΙΔΑ|Σελίδα\s*[0-9]+\)?")
selida_num_regex = re.compile(r"\(?(ΣΕΛΙΔΑ|Σελίδα)\s*\d+\)?")

log_file = open('./no_xml_files.txt', 'a', encoding="utf8")


for filename in filenames:
    try:
        # ------- AKOMA NTOSO/xml ---
        d = Debate()
        # remove default-useless debateSection
        d.debateBody.remove(d.debateBody.debateSection[0])
        d.debateBody.attrib.pop("eId")
        speech_num = 0
        # ----- meta references ---
        d.meta.references.TLCOrganization.attrib["eId"] = "greek_parl"
        d.meta.references.TLCOrganization.attrib["href"] = "/ontology/organization/akn/greek_parl"
        d.meta.references.TLCOrganization.attrib["showAs"] = "Greek_Parliament"
        meta_proedros = create_meta_references_akn("TLCRole", "ΠΡΟΕΔΡΟΣ")
        d.meta.references.append(meta_proedros)
        parsed = parser.from_file(datapath+filename, xmlContent=True)
        parsed1true = False
        # parsed = parsed1
        record_counter += 1
        # if record_counter < 1320:
        #     continue
        # print(record_counter, ":", filename)
        if (record_counter % 350 == 0):
            print("File "+str(record_counter)+' from ' +
                  str(len(filenames)) + ' '+filename)

        # Skip duplicate files
        # new_name = '_'.join([p for p in filename.split('_') if p!=(filename.split('_')[1])])
        new_name = "_".join([str(record_counter), filename])
        filename_freqs[new_name] += 1
        if filename_freqs[new_name] > 1:
            continue  # with next iteration of for loop

        content = parsed['content']
        soup = BeautifulSoup(content, 'html.parser')
        # remove header-footer of a docx file
        div_header = soup.find('div', class_='header')
        div_footer = soup.find('div', class_='footer')
        if div_header:
            div_header.decompose()
        if div_footer:
            div_footer.decompose()
        f3 = soup.body.get_text()
        f3 = re.sub(selida_num_regex, "", f3)
        f3_last = re.sub(r'\n\s*\n', '\n', f3)

        split_text = re.split(r"(Αθήνα\,?\s*σήμερα\,?)\s*", f3_last)
        introduction = split_text[0]
        main_text = split_text[1] + " " + split_text[2]
        introduction = re.sub(r'σελ\.?\s+', 'σελ.\n', introduction)
        main_text = re.sub(r'Επιστροφή\s*στην\s*κορυφη\s*', '', main_text)
        # Creates a list of tuples e.g. (' ΠΡΟΕΔΡΕΥΩΝ (Βαΐτσης Αποστολάτος):', ' ΠΡΟΕΔΡΕΥΩΝ', '', '(Βαΐτσης Αποστολάτος)')
        speakers_groups = re.findall(
            r"(([Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)(\s+\([Α-ΩΆ-Ώα-ωά-ώϊϋΐΰΪΫΪ́Ϋ́-]+\))?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́.]+)?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)*\s*(\(.*?\))?\s*\:)",
            # r"(([Α-ΩΆ-ΏΪΫΪ́Ϋ́-]{2,})+(\s+\([Α-ΩΆ-Ώα-ωά-ώϊϋΐΰΪΫΪ́Ϋ́-]+\))?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́.]+)?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)*\s*(\(.*?\))?\s*\:\s)",
            main_text.split('\n', 1)[1])

        # --- ANTLR4 parameters
        input_stream = InputStream(introduction)
        lexer = DebateGrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser_grammar = DebateGrammarParser(token_stream)
        tree = parser_grammar.start()
        set_record_values(tree)
        current_record_datetime = get_date(record_date)
        # print(current_record_datetime)
        edit_meta_debate_akn(current_record_datetime)
        create_preface_akn(d, tree)

        debateSection_preamble = create_preamble_akn(
            main_text.split('\n', 1)[0], name="opening")
        d.main_content.append(debateSection_preamble)
        debateSection_main = create_debateSection_akn()
        d.main_content.append(debateSection_main)

        # Keep only first full match case of findall
        speakers = [speaker[0] for speaker in speakers_groups]

        # Delete words that are not speakers
        name_for_delete = ['ΝΑΙ', 'ΠΡΑΚΤΙΚΩΝ', 'ΔΗ.ΣΥ', 'ΟΚΕ:', 'ΠΕΡΙΘΑΛΨΗ', 'ΑΣΦΑΛΕΙΑΣ', 'ΕΠΙΣΚΕΨΗ',
                           'ΕΠΙΚΟΙΝΩΝΙΑ', 'ΟΔΑΠ', 'ΒΑΘΜΟΣ', 'ΕΤΒΑ:', 'ΑΧΑΙΑ', 'ΑΔΕΔΥ', 'ΟΑΚΑ', 'ΑΚΕ:', 'ΟΔΙΕ:', 'ΕΠΑΛ:', 'ΕΙΔΙΚΟΤΕΡΑ',
                           'ΕΠΙΚΥΡΩΣΗ', 'Χ.Α:', 'ΚΑΠΑ:', 'ΥΓΕΙΟΝΟΜΙΚΗ', 'ΜΕΤΡΑ', 'ΣΧΟΛΕΙΟ', 'ΥΓΙΕΙΝΗ', 'ΑΘΗΝΑ', 'Χ.Δ.', 'ΑΤΕ:', 'ΗΜΑΘΙΑ',
                           'ΤΗΛΕΦΩΝΟ', 'ΚΔΑΥ', 'ΚΥΘΗΡΑ', 'ΡΑΦΗΝΑ:', 'ΤΣΧ:', 'ΑΛΛΕΣ ΧΩΡΕΣ', 'ΟΧΙ', 'ΣΥΝΟΛΙΚΑ', 'ΔΕΣΥ:', 'ΕΟΤ', 'ΑΔΕΙΕΣ', 'ΚΤΙΡΙΑΚΕΣ',
                           'ΜΚΟ', 'ΣΙΤΙΣΗ', 'ΙΕΚ', 'ΚΟΙΝ:', '-ΤΕΛΕΧ:', 'ΧΑΛΚΙΔΙΚΗ', 'ΠΑΕ', 'ΔΙΑΝΟΜΗ', 'ΟΣΕ:', 'ΔΝΤ:', 'ΜΑΤ:', 'ΠΡΟΑΣΤΙΑ', 'ΠΡΝ',
                           'ΨΗΦΟΙ', 'Α.Π', 'ΥΠΕΠΘ', 'ΣΩΦΡΟΝΙΣΜΟΣ', 'ΚΡΑΤΟΥΜΕΝΕΣ', 'ΥΠΕΡΠΛΗΘΥΣΜΟΣ', 'ΣΙΤΙΣΗ', 'ΕΒΕΑ', 'ΟΤΑ:', 'ΕΥΠ:', 'ΑΔΜΗΕ',
                           'ΕΞΟΔΟ', 'Κ.Κ.Ε', 'ΕΣΠΑ', 'Α.Β.Ε.Ε.', 'ΑΙΤΗΜΑΤΑ', 'ΑΝΗΛΙΚΟΙ', 'ΠΡΑΞΗ', 'ΣΑΠΘ', 'ΕΣΟΘΕ', 'ΥΠΕΘΟ:', 'ΜΕΣΣΗΝΙΑ', 'ΕΥΒΟΙΑ',
                           'ΚΤΕΟ:', 'ΝΟΜΑΡΧΙΑ', 'ΕΤΕΒΑ:', 'ΣΔΙΤ:', 'ΑΧΕΠΑ:', 'ΚΚΕ:', 'ΦΠΑ', 'ΤΚΑΣΕ:', 'ΧΡΟΝΟΣ', 'ΝΕΡΟ', 'ΠΑΔΑ', 'ΕΟΔΥ', 'ΤΕΑΕΔΞΕ',
                           'ΚΑΣΤΟΡΙΑ', 'ΩΡΛ:', 'ΜΜΕ:', 'ΥΓΡΑ', 'ΚΕΔΚΕ:', 'ΟΗΕ:', 'ΡΑΣ:', 'ΣΥΡΙΖΑ:',  'ΠΕΚ', 'ΣΩΦΡΟΝΙΣΤΙΚΟ', 'ΕΡΤ:', 'ΔΥΝΑΜΙΚΟΤΗΤΑ', 'ΑΩ:',
                           'ΕΦΚΑ', 'ΕΝΑ:', 'ΛΑΡΙΣΑ',  'ΑΠΟ:', 'ΛΕΥΚΑ:', 'ΦΟΡΕΑΣ', 'ΕΛΕΥΘΕΡΟΤΥΠΙΑ', 'ΟΛΠ:', 'ΜΕΤΡΟ ', 'ΑΤΤΙΚΗ', 'ΚΥΚΛΑΔΕΣ', 'ΙΚΑ:', 'ΕΡΓΟ:',
                           'ΟΝΕ:', 'ΕΚΑΣ:', 'ΝΑΤΟ:', 'ΔΗΜΑΡΧΟΙ', 'Ν.Δ.:',  'ΧΗΤΟΣ', 'ΠΡΟΤΑΣΕΙΣ', 'ΧΩΡΗΤΙΚΟΤΗΤΑ', 'ΕΥΚΑΙΡΙΑΣ', 'ΠΟΙΝΕΣ', 'ΑΦΜ:', 'ΠΑΘΕ:',
                           'ΔΡΑΜΑ', 'ΒΟΙΩΤΙΑ', 'ΕΥΔΑΠ', 'ΠΟΛΥ', 'ΔΕΚ:', 'ΕΛΚΕ:', 'ΔΗΣΥ:', 'ΕΝΦΙΑ', 'ΔΕΗ', 'ΚΑΤΑΣΤΗΜΑ', 'ΤΜΗΜΑ', 'ΕΕ:', 'ΑΑ:', 'ΤΕΒΕ', 'ΛΟΙΠΑ ΕΡΓΑ',
                           'ΠΕΛΛΑ', 'ΟΤΕ:', 'ΥΠΟΨΗ:', 'ΤΡΟΙΖΗΝΙΑ', 'ΑΕΚ:', 'ΕΣΡ:', 'ΤΑΜΕΙΟ', 'ΕΝ.', 'ΘΕΜΑ', 'ΑΣΕΠ', 'ΩΡΑ:', 'ΠΑΡΑΡΤΗΜΑ', 'ΣΧΕΤ', 'ΓΔΕ:', 'ΔΗΜΑΡΧΟΙ',
                           'ΤΑΧΔΙΚ', 'ΜΑΓΝΗΣΙΑ', 'ΤΟΕΒ', 'ΟΕΔΒ', 'ΑΜΥ', 'ΜΕΘ:', 'ΕΝΤΥΠΑ', 'ΠΕΧΩΔΕ', 'ΚΡΑΤΟΥΜΕΝΟΙ', 'ΑΦΙΞΗΣ', 'ΙΓΜΕ:', 'ΕΛΤΑ', 'ΣΚΟΠΙΕΣ', '-ΜΚΙΙ:',
                           'ΤΗΛΕΦ', 'ΣΑΕ', 'ΥΩΝ:', 'ΟΟΣΑ', 'ΝΟΜΟΣ', 'ΕΛΣΤΑΤ:', 'ΤΗΛΕΟΡΑΣΗ', 'ΚΕΝΤΡΩΩΝ', 'ΠΡΟΣ', 'ΔΙΑΒΙΩΣΗ', 'ΥΠΕ:', 'ΡΑΔΙΟΦΩΝΟ', 'ΕΟΚ', 'ΣΙΤΗΣΗ', 'ΣΕΠ:', 'ΟΓΑ:',
                           'Α.Π.:', 'ΙΡΑΝ', 'ΕΚΑΒ', 'ΠΕΠΕΡ:', 'ΕΛΓA:', 'ΕΡΓΑΣΙΑ', 'ΕΛΛΗΝΙΚΗ ΛΥΣΗ:', 'ΓΡΑΜΜΑΤΕΙΣ', 'ΜΕΛΗ', 'ΣΕΠΕ', 'ΣΕΛΕΤΕ', 'ΑΡΘΡΟ', 'ΑΕΙ:', 'ΕΠΕ:', 'ΠΑΣΟΚ', 'ΤΟΥ ΠΑ.ΣΟ.Κ.:',
                           'ΗΔΙΚΑ:', 'ΕΣΟΔΑ', 'ΣΕΚ', 'ΔΕΠΑΝΟΜ', 'ΠΛΗΡΟΦΟΡΙΕΣ', 'ΑΕΠΠ:', 'ΤΗΛ.', 'ΚΠΣ', 'ΟΑΕ', 'ΙΡΑΝ', 'ΜΕΤΑΓΩΓΕΣ']

        # remove extra spaces inside names
        speakers = [s.strip() for s in speakers if not any(
            sub in s for sub in name_for_delete)]

        # for example if "NAME. \nPROEDROS(NAME):"
        speakers = [item.split(
            '\n')[1] if '\n' in item else item for item in speakers]
        # for i in range(len(speakers)):
        #     print(speakers[i])
        speakers_noDublicates = list(set(speakers))
        speakers_noDublicates = [format_speaker_information(
            speaker, '', True)[0] for speaker in speakers_noDublicates]
        speakers_noDublicates = list(set(speakers_noDublicates))
        for speaker in speakers_noDublicates:
            meta_references = create_meta_references_akn("TLCPerson", speaker)
            d.meta.references.append(meta_references)

        if (allagi_selidas.search(speaker)):
            # print(allagi_selidas.search(speaker).group())
            speaker = speaker.replace(
                allagi_selidas.search(speaker).group(), '')
        # print(len(speakers))
        main_text = main_text.split('\n', 1)[1]
        main_text = main_text.split(speakers[0], 1)[1]
        for i in range(len(speakers)):
            # print the "id" of current speaker (testing)
            # if (i % 100 == 0):
            #     print(i)
            # If not last speaker
            if i < (len(speakers)-1):
                speaker = speakers[i]
                speech, main_text = main_text.split(speakers[i+1], 1)
            else:
                speaker = speakers[i]
                speech = main_text

            # remove parenthesis text which is usually descriptions of procedures
            # speech = re.sub(text_in_parenthesis, " ", speech)
            if (allagi_selidas.search(speech)):
                # print(allagi_selidas.search(speech).group())
                speech = speech.replace(
                    allagi_selidas.search(speech).group(), '')

            # Clean speaker
            speaker = speaker.strip()
            speaker = re.sub("\s\s+", " ", speaker)

            speaker_info = np.nan
            speaker_nickname = ''
            # in case the speaker name is like "ΠΡΟΕΔΡΕΥΩΝ (Παναγιώτης Ν. Κρητικός):"
            # or like ΠΡΟΣΩΡΙΝΟΣ ΠΡΟΕΔΡΟΣ (Ιωάννης Τραγάκης):
            if proedr_regex.search(speaker):

                # Hand-picked wrong cases
                if any(mistaken in speaker for mistaken in ['ΤΗΛΕΦΩΝΟ', 'ΓΡΑΜΜΑΤΕΙΣ', 'ΠΡΟΕΚΟΠΗΣ']):
                    continue  # to next iteration/speaker

                # For proedreuon
                if not proedros_regex.search(speaker):
                    speaker_info = 'προεδρευων'

                # For proedros
                else:
                    # if the person in proedros
                    if 'ΠΡΟΣΩΡΙΝ' in speaker:
                        speaker_info = 'προσωρινος προεδρος'
                    else:
                        speaker_info = 'προεδρος'

                segments = speaker.split('(')
                speaker = ''.join(segments[1:])

                # for cases where the name of the person is not mentioned
                if len(speaker) < 3:
                    speaker = np.nan
                    continue  # to next iteration/speaker

            if speaker.startswith('ΜΑΡΤΥΣ'):
                speaker = speaker.replace('ΜΑΡΤΥΣ', '')
                speaker = re.sub("[()]", '', speaker)
                speaker_info = 'μαρτυς'

                if len(speaker) < 3:  # for cases where the name of the person is not mentioned
                    speaker = np.nan
                    continue  # to next iteration/speaker

            if general_member_regex.search(speaker):
                speaker = (re.sub("[():'’`΄‘.]", '', speaker))
                speaker = speaker.translate(
                    str.maketrans('άέόώήίϊΐiύϋΰ', 'αεοωηιιιιυυυ'))
                if 'εφηβοι' in speaker:
                    continue  # to next speaker
                else:
                    speaker = np.nan
                    speaker_info = 'βουλευτης/ες'
                    roles = np.nan
                    speech_num += 1
                    debateSectionParts = create_speeches_akn(
                        speaker=speaker_info, speeches=speech, num=speech_num)
                    debateSection_main.append(debateSectionParts)
                    continue

            # continue
            if speaker != '':
                # Exclude very large malformed text that is not a speaker
                if len(speaker) < 200:
                    speaker_name, speaker_info, speaker_nickname = format_speaker_information(
                        speaker, speaker_nickname)

                    # Remove 1-2 letter characters
                    speaker_name = ' '.join(
                        [word for word in speaker_name.split(' ') if len(word) > 2])

                    cm = comment_sto_simio_auto.search(speech)
                    xeir = xeirokrotima.search(speech)
                    if (cm or xeir):
                        if (cm):
                            regex_finded = comment_sto_simio_auto
                            part_splited = 4
                        elif (xeir):
                            regex_finded = xeirokrotima
                            part_splited = 3
                        splited_text = re.split(regex_finded, speech)
                        # print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                        #        record_period, record_session, record_sitting, max_member_party,
                        #        current_gov, max_member_region, max_member_roles, max_member_gender,
                        #        speaker_info])
                        # print(splited_text[0])
                        speech_num += 1
                        debateSectionParts = create_speeches_akn(
                            speaker=speaker_name, speeches=splited_text[0], num=speech_num)
                        debateSection_main.append(debateSectionParts)
                        assd = regex_finded.search(speech).group()
                        debateSectionParts = create_scene_akn(
                            xeir_sxolio=assd)
                        debateSection_main.append(debateSectionParts)
                        if (len(splited_text[part_splited]) > 1):
                            # print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                            #        record_period, record_session, record_sitting, max_member_party,
                            #        current_gov, max_member_region, max_member_roles, max_member_gender,
                            #        speaker_info])
                            # print(splited_text[part_splited])
                            speech_num += 1
                            debateSectionParts = create_speeches_akn(
                                speaker=speaker_name, speeches=splited_text[part_splited], num=speech_num)
                            debateSection_main.append(debateSectionParts)
                    else:
                        # print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                        #        record_period, record_session, record_sitting, max_member_party,
                        #        current_gov, max_member_region, max_member_roles, max_member_gender,
                        #        speaker_info])
                        speech_num += 1
                        debateSectionParts = create_speeches_akn(
                            speaker=speaker_name, speeches=speech, num=speech_num)
                        debateSection_main.append(debateSectionParts)
                if (ilektroniki_katametrisi_regex.search(speech)):
                    speech_num += 1
                    debateSectionParts = create_speeches_akn(
                        speaker="ΠΡΟΕΔΡΟΣ", speeches=ilektroniki_katametrisi_regex.search(speech).group(), num=speech_num)
                    debateSection_main.append(debateSectionParts)
                    speech = speech.replace(
                        ilektroniki_katametrisi_regex.search(speech).group(), '')

        xml1 = d.to_xml(encoding='unicode', pretty_print=True)
        # print(xml1)

        # print("---------------------")
        # ---- saving xml to a differnt file
        text_file = open("../xml_akn_files/"+filename +
                         ".xml", "w", encoding='utf8')
        # text_file = open("./testing.xml", "w", encoding='utf8')
        n = text_file.write(xml1)
        text_file.close()

    except Exception as e:
        log_file.write(f'{filename}: {str(e)}\n')
        # print(filename, ":", traceback.format_exc())
    if parsed1true:
        break
log_file.close()
endtime = dt.now()
print("-----------------")
print(endtime-starttime)
print("-----------------")
