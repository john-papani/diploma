
from lxml.builder import ElementMaker
from lxml import etree as ET
from cobalt import Debate
from antlr4 import *
from tika import parser
import ast
import pandas as pd
from datetime import datetime as dt
import numpy as np
from collections import defaultdict
import jellyfish
import re
import os
from bs4 import BeautifulSoup
import sys
sys.path.insert(1, '../antlr4_python')

from DebateGrammarParser import DebateGrammarParser
from DebateGrammarLexer import DebateGrammarLexer
E = ElementMaker(nsmap={None: 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'},
                 namespace='http://docs.oasis-open.org/legaldocml/ns/akn/3.0')


'''This script extracts speeches from record files and matches them to the
official parliament or government member from the file all_members_activity.csv.
The script takes as arguments from the command line
1) The path of the folder with the record files
2) The path to the folder where it outputs the speeches and the corresponding speakers
Example: python member_speech_matcher.py -f '../path/to/data/folder/' -o '../output/folder/tell_all.csv'
'''


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


def create_speeches_akn(speaker, speeches):
    speaker_englishVersion = convert_greek_to_english(speaker)
    speech_ = speeches.split("\n")
    speech_.pop()
    paragraphs = [E.p(speech_[i].strip()) for i in range(len(speech_))]
    speech = E.speech(
        ET.XML(f"<from>{str(speaker)}</from>"),
        *paragraphs, by=f"{speaker_englishVersion}"
    )
    return speech


def create_preamble_akn(preamble_text, name="preamble"):
    preamble = E.p(preamble_text.strip())
    debateSection = (
        E.debateSection(name=name))
    debateSection.append(preamble)
    return debateSection


def create_meta_references(type, name):
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


def edit_meta_debate_akn(current_record_date):
    date_ = current_record_date.strftime('%Y-%m-%d')
    d.expression_date = str(date_)
    d.manifestation_date = str(date_)
    d.manifestation_format = "xml"
    d.frbr_uri = "/akn/gr-ath/debate/"+str(date_)+"/1/"
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


# for example ΠΟΛΛΟΙ ΒΟΥΛΕΥΤΕΣ (από την πτέρυγα του ΠΑ.ΣΟ.Κ.):...
def party_of_generic_reference(speaker):

    if 'πασοκ' in speaker:
        party = 'πανελληνιο σοσιαλιστικο κινημα'
    elif 'δημοκρατια' in speaker:
        party = 'νεα δημοκρατια'
    elif 'συνασπισμου' in speaker:
        party = 'συνασπισμος της αριστερας των κινηματων και της οικολογιας'
    elif 'λαος' in speaker:
        party = 'λαικος ορθοδοξος συναγερμος'
    elif 'συριζα' in speaker:
        party = 'συνασπισμος ριζοσπαστικης αριστερας'
    elif 'αντιπολιτευσ' in speaker:
        party = 'αντιπολιτευση'
    else:
        party = 'βουλη'
    return party


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


# compare temp max with similarity of the member's name alternatives with the speaker name
def compare_with_alternative_sim(speaker_name, member_name, member_surname, temp_max, greek_names):

    # each row in the greek_names data is unique concerning the first name of the row
    # greek_names has only those names that have at least one alternative. so each line has at least two names
    for line in greek_names:

        name_list = (line.strip()).split(',')

        # if member name has alternatives
        if name_list[0] == member_name:

            # keep alternatives of the name
            name_list.remove(member_name)

            for alternative_name in name_list:
                alternative_sim1 = jellyfish.jaro_winkler_similarity(
                    speaker_name, alternative_name+' '+member_surname)
                alternative_sim2 = jellyfish.jaro_winkler_similarity(
                    speaker_name, member_surname + ' ' + alternative_name)
                temp_max = max(temp_max, alternative_sim1, alternative_sim2)

            break  # if true, break the for loop and proceed to return temp pax

    return temp_max


def get_gov(current_record_datetime):

    df_govs = pd.read_csv(
        "C:/Users/johnp/Documents/ECE_NTUA/diploma/dipoma_code/diploma_python_data_scrapping/more_files/governments_1989onwards.csv", encoding='utf-8')
    df_govs['date_from'] = pd.to_datetime(df_govs['date_from'])  # .dt.date
    df_govs['date_to'] = pd.to_datetime(df_govs['date_to'])  # .dt.date
    df_govs = df_govs.sort_values(by='date_from', ascending=True)
    current_gov_df = df_govs.loc[(df_govs.date_from <= current_record_datetime) & (
        current_record_datetime < df_govs.date_to)]
    print(current_gov_df)
    if current_gov_df.shape[0] != 1:
        print('problem with ', current_record_datetime)
    print(current_record_datetime)
    item = current_gov_df.gov_name.iloc[0] + '(' + current_gov_df.date_from.iloc[0].strftime('%d/%m/%Y') +\
        '-' + current_gov_df.date_to.iloc[0].strftime('%d/%m/%Y') + ')'

    return [item]


def keep_roles_at_date(roles, current_record_datetime):

    new_roles = []

    # assert type list
    if type(roles) != list:
        roles = ast.literal_eval(roles)

    for role in roles:
        role_name, role_dates = role.split('(')
        role_start_date, role_end_date = role_dates.replace(')', '').split('-')
        role_start_date = dt.strptime(role_start_date, '%d/%m/%Y')
        role_end_date = dt.strptime(role_end_date, '%d/%m/%Y')
        if role_start_date <= current_record_datetime <= role_end_date:
            new_roles.append(role)

    # if empty list
    if not new_roles:
        new_roles.append('βουλευτης')

    return new_roles


def compute_max_similarity(speaker_name, speaker_nickname, member_name_part):
    speaker_name = speaker_name.lower()
    if ('(' in member_name_part and len(member_name_part.split(' ')) > 3) or ('(' not in member_name_part and len(member_name_part.split(' ')) > 2):
        member_surname = member_name_part.split(' ')[0]
        member_name = member_name_part.split(' ')[2]
    else:  # εξωκοινοβουλευτικος χωρις ονομα πατρος
        member_surname = member_name_part.split(' ')[1]
        member_name = member_name_part.split(' ')[0]
    temp_max = 0

    # put these transpositions in the beginning, before we remove '-'
    # If member has more than one first names
    if '-' in member_name:
        # there are cases like member name being δενδιας νικολαος-γεωργιος
        # and detected speaker being ΝΙΚΟΛΑΟΣ ΔΕΝΔΙΑΣ

        # if member has two first names
        if len(member_name.split('-')) == 2:
            member_name1, member_name2 = member_name.split('-')

        # if member has three first names
        elif len(member_name.split('-')) == 3:
            member_name1, member_name2, member_name3 = member_name.split('-')

        # if member has more than one first names and one surname
        if '-' not in member_surname:
            # do the following for two first names
            sim5 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name1 + ' '+member_surname)
            sim6 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname+' '+member_name1)
            sim7 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name2 + ' '+member_surname)
            sim8 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname+' '+member_name2)

            temp_max = max(temp_max, sim5, sim6, sim7, sim8)
            # Extra comparisons for alternative names of members
            # temp_max = compare_with_alternative_sim(speaker_name, member_name1, member_surname, temp_max, greek_names)
            # temp_max = compare_with_alternative_sim(speaker_name, member_name2, member_surname, temp_max, greek_names)

            # do the following extra for three first names
            # for example κουικ φιλιππου τερενς-σπενσερ-νικολαος
            if len(member_name.split('-')) == 3:
                sim9 = jellyfish.jaro_winkler_similarity(
                    speaker_name, member_name3 + ' '+member_surname)
                sim10 = jellyfish.jaro_winkler_similarity(
                    speaker_name, member_surname + ' '+member_name3)
                temp_max = max(temp_max, sim9, sim10)
                # Extra comparisons for alternative names of members
                # temp_max = compare_with_alternative_sim(speaker_name, member_name3,
                #                                         member_surname, temp_max,
                #                                         greek_names)

        else:
            # If member has more than one first names and two surnames, compare each one separately
            member_surname1, member_surname2 = member_surname.split('-')
            sim5 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name1 + ' '+member_surname1)
            sim6 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname1+' '+member_name1)
            sim7 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name1+' '+member_surname2)
            sim8 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname2+' '+member_name1)
            sim9 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name2+' '+member_surname1)
            sim10 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname1+' '+member_name2)
            sim11 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_name2+' '+member_surname2)
            sim12 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname2+' '+member_name2)

            temp_max = max(temp_max, sim5, sim6, sim7,
                           sim8, sim9, sim10, sim11, sim12)
            # there is no case with 3 first names and 2 last names, so we don't compute that

            # Extra comparisons for alternative names of members
            # temp_max = compare_with_alternative_sim(speaker_name, member_name1, member_surname1, temp_max, greek_names)
            # temp_max = compare_with_alternative_sim(speaker_name, member_name1, member_surname2, temp_max, greek_names)
            # temp_max = compare_with_alternative_sim(speaker_name, member_name2, member_surname1, temp_max, greek_names)
            # temp_max = compare_with_alternative_sim(speaker_name, member_name2, member_surname2, temp_max, greek_names)

    # If member has one first name and two surnames
    elif '-' in member_surname:
        member_surname1, member_surname2 = member_surname.split('-')
        sim5 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_name+' '+member_surname1)
        sim6 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_surname1+' '+member_name)
        sim7 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_name+' '+member_surname2)
        sim8 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_surname2+' '+member_name)

        temp_max = max(temp_max, sim5, sim6, sim7, sim8)

        # Extra comparisons for alternative names of members
        # temp_max = compare_with_alternative_sim(speaker_name, member_name, member_surname1, temp_max, greek_names)
        # temp_max = compare_with_alternative_sim(speaker_name, member_name, member_surname2, temp_max, greek_names)

        # If member has available nickname and two surnames
        if lower_nickname_in_parenthesis.search(member_name_part) and speaker_nickname == '':

            member_nickname = re.sub(
                '[()]', '', (lower_nickname_in_parenthesis.search(member_name_part)).group())
            sim9 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_nickname+' '+member_surname1)
            sim10 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname1+' '+member_nickname)
            sim11 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_nickname+' '+member_surname2)
            sim12 = jellyfish.jaro_winkler_similarity(
                speaker_name, member_surname2+' '+member_nickname)

            temp_max = max(temp_max, sim9, sim10, sim11, sim12)

    # Remove '-' for sim1, sim2 best comparisons
    member_name = member_name.replace('-', ' ')
    member_surname = member_surname.replace('-', ' ')

    # Make comparisons of speaker with members' names and reversed members' names
    sim1 = jellyfish.jaro_winkler_similarity(
        speaker_name, member_name+' '+member_surname)
    sim2 = jellyfish.jaro_winkler_similarity(
        speaker_name, member_surname+' '+member_name)
    temp_max = max(temp_max, sim1, sim2)

    # Extra comparisons for alternative names of members
    # temp_max = compare_with_alternative_sim(speaker_name, member_name, member_surname, temp_max, greek_names)

    # We compare speaker with member's nickname and surname
    if lower_nickname_in_parenthesis.search(member_name_part) and speaker_nickname == '':

        member_nickname = re.sub(
            '[()]', '', (lower_nickname_in_parenthesis.search(member_name_part)).group())
        sim3 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_nickname+' '+member_surname)
        sim4 = jellyfish.jaro_winkler_similarity(
            speaker_name, member_surname+' '+member_nickname)

        temp_max = max(temp_max, sim3, sim4)

    return temp_max


def month_to_number(month):

    months = {'ιανουαριου': '1', 'φεβρουαριου': '2', 'μαρτιου': '3',
              'απριλιου': '4', 'μαιου': '5', 'ιουνιου': '6', 'ιουλιου': '7',
              'αυγουστου': '8', 'σεπτεμβριου': '9', 'οκτωβριου': '10',
              'νοεμβριου': '11', 'δεκεμβριου': '12'}

    return months[month]


def get_date(date):
    year = date.split()[3]
    day = date.split()[1]
    month = date.split()[2]
    month = month.translate(str.maketrans(
        'άΆέΈόΌώΏήΉίΊϊΐύΎϋΰ', 'αΑεΕοΟωΩηΗιΙιιυΥυυ')).lower()  # remove accents&lower
    month = month_to_number(month)
    date = dt.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
    return date


def set_record_values(table_of_content):
    input_stream = InputStream(table_of_content)
    lexer = DebateGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DebateGrammarParser(token_stream)
    tree = parser.start()
    tree_parlDetails = tree.parliament_proceedings().parliament_detail()

    # Extract parliament details
    anatheoritiki_bouli = tree_parlDetails.anatheoritiki_bouli().getText(
    ) if tree_parlDetails.anatheoritiki_bouli() is not None else None
    period_detail = tree_parlDetails.period_detail().getText(
    ) if tree_parlDetails.period_detail() is not None else None
    dimokratia = tree_parlDetails.dimokratia().getText(
    ) if tree_parlDetails.dimokratia() is not None else None
    sunodos = tree_parlDetails.sunodos().getText(
    ) if tree_parlDetails.sunodos() is not None else None
    ergasies = tree_parlDetails.ergasies().getText(
    ) if tree_parlDetails.ergasies() is not None else None
    sunedriasi = tree_parlDetails.sunedriasi().getText(
    ) if tree_parlDetails.sunedriasi() is not None else None
    date = tree_parlDetails.date().getText(
    ) if tree_parlDetails.date() is not None else None
    # print("==--=-", date, "-=-=-")
    global record_date, record_period, record_session, record_sitting
    record_date = date
    record_period = period_detail
    record_session = sunodos
    record_sitting = sunedriasi


datapath = "C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/files/"
parsed = parser.from_file(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/files/2018__test.docx', xmlContent=True)

# print(parsed["metadata"]["dcterms:created"])
# print(parsed["content"])
# f1_path = args.outpath
# f2_path = args.outpath2

# # Goal file with all members speeches
# f1 = open(f1_path, 'w+', encoding='utf-8', newline = '')

members_df = pd.read_csv(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/dipoma_code/diploma_python_data_scrapping/more_files/all_members_activity.csv', encoding='utf-8')

# fnames = open("C:/Users/johnp/Documents/ECE_NTUA/diploma/GreekParliementProceedingsDritsaOPA/Parliament Proceedings Dataset_Support Files_Word Usage Change Computations/wiki_data/female_name_cases_populated.json", 'r+', encoding='utf-8')
# greek_names = fnames.readlines()

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
    r"\(\s*(Σ|σ)το σημε(ί|ι)ο αυτ(ό|ο).*?\){1}")
xeirokrotima = re.compile(r"\((χ|Χ)ειροκροτ(ή|η)ματα .*?\)")
allagi_selidas = re.compile(r"\(?ΑΛΛΑΓ(Η|Ή)\s*ΣΕΛ(Ι|Ί)ΔΑΣ\s*[Α-Ω]*\)")
starting_regex = re.compile(
    r"(Π\s*Ρ\s*Α\s*Κ\s*Τ\s*Ι\s*Κ\s*(Α|A)\s*(Τ\s*Η\s*Σ)?\s*Β\s*Ο\s*Υ\s*Λ\s*Η\s*Σ)\s*(.+)('|΄|`|’)\s*ΠΕΡΙΟΔΟΣ\s*\(?((ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)|(ΠΡΟΕΔΡΕΥ?Ο?ΜΕΝΗΣ? ΔΗΜ?ΟΚΡΑΤΙΑΣ))\)?\s*(Σ\s*Υ\s*Ν\s*Ο\s*Δ\s*Ο\s*Σ)?\s*(.+)('|΄|`|’)\s+(.*)\s*(Σ\s*Υ\s*Ν\s*Ε\s*Δ\s*Ρ\s*Ι\s*Α\s*Σ\s*Η|ΣΥΕΝΔΡΙΑ|Συνεδρίαση|ΣΥΕΝΔΡΙΑΣΗ)\s*(([Α-Ω]*)(΄|'|`|’)?)\s*([\u0386-\u03CE]+\s*,? \s*\d{1,2} \n*[\u0386-\u03CE]+\s*\d{4})")
preamble_regex = re.compile(r"(Αθήνα.*)")
ilektroniki_katametrisi_regex = re.compile(
    r"(\([Α-Ωα-ω\s]*ΗΛΕΚΤΡΟΝΙΚΗ\s*ΚΑΤΑ[Α-Ωα-ω]*\))")

selida_num_regex = re.compile(r"\(ΣΕΛΙΔΑ|Σελίδα [0-9]+\)")

# csv_output = csv.writer(f1)

# # csv header
# csv_output.writerow(['member_name', 'sitting_date', 'parliamentary_period',
#                      'parliamentary_session','parliamentary_sitting',
#                      'political_party', 'government', 'member_region', 'roles', 'member_gender',
#                      'speaker_info', 'speech'])

# Open a file in order to write down the rows with no files


# ------- AKOMA NTOSO/xml ---

d = Debate()
# ----- meta references ---
d.meta.references.TLCOrganization.attrib["eId"] = "greek_parl"
d.meta.references.TLCOrganization.attrib["href"] = "/ontology/organization/akn/greek_parl"
d.meta.references.TLCOrganization.attrib["showAs"] = "Greek_Parliament"


prob_files = open('./out_files/files_with_content_problems_' +
                  os.path.basename(os.path.normpath(datapath))+'.txt', 'w+',
                  encoding='utf-8')
log_file = open('./BIG_PROBLEM_1.txt', 'a')
for filename in filenames:
    # parsed = parser.from_file(datapath+filename, xmlContent=True)
    record_counter += 1
    if (record_counter % 350 == 0):
        print("File "+str(record_counter)+' from ' +
              str(len(filenames)) + ' '+filename)

    # Skip duplicate files
    # new_name = '_'.join([p for p in filename.split('_') if p!=(filename.split('_')[1])])
    new_name = "_".join([str(record_counter), filename])
    filename_freqs[new_name] += 1
    if filename_freqs[new_name] > 1:
        continue  # with next iteration of for loop

    # name_parts_without_extension = (os.path.splitext(filename)[0]).split('_')
    # record_year = record_date.split('-')[0].strip()
    # current_record_datetime = dt.strptime(record_date, '%Y-%m-%d')
    # current_gov = get_gov(current_record_datetime)

    # f3 = open(os.path.join(datapath+filename), 'r', encoding='utf-8')

    content = parsed['content']
    soup = BeautifulSoup(content, 'html.parser')
    f3 = soup.body.get_text()
    f3 = re.sub(selida_num_regex, "", f3)
    split_text = re.split(r"(Αθήνα\,? σήμερα\,?)\s*", f3)
    introduction = split_text[0]
    main_text = split_text[1] + split_text[2]

    # Creates a list of tuples e.g. (' ΠΡΟΕΔΡΕΥΩΝ (Βαΐτσης Αποστολάτος):', ' ΠΡΟΕΔΡΕΥΩΝ', '', '(Βαΐτσης Αποστολάτος)')
    speakers_groups = re.findall(
        r"((\s*[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]{2,})+(\s+\([Α-ΩΆ-Ώα-ωά-ώϊϋΐΰΪΫΪ́Ϋ́-]+\))?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́.]+)?(\s+[Α-ΩΆ-ΏΪΫΪ́Ϋ́-]+)*\s*(\(.*?\))?\s*\:)",
        main_text)
    # file_content = main_text.replace('\n', ' ')
    # file_content = re.sub("\s\s+", " ", file_content)
    set_record_values(introduction)
    current_record_datetime = get_date(record_date)
    edit_meta_debate_akn(current_record_datetime)

    debateSection_preamble = create_preamble_akn(
        main_text.split('\n', 1)[0], name="opening")
    d.main_content.append(debateSection_preamble)
    debateSection_main = create_debateSection_akn()
    d.main_content.append(debateSection_main)

    current_gov = get_gov(current_record_datetime)

    # Keep only first full match case of findall
    speakers = [speaker[0] for speaker in speakers_groups]



    # Delete words that are not speakers
    name_for_delete = ['ΝΑΙ:', 'ΟΧΙ:', 'ΠΡΝ:',
                       'ΕΠΙΚΥΡΩΣΗ ΠΡΑΚΤΙΚΩΝ:', 'ΣΥΝΟΛΙΚΑ ΨΗΦΟΙ:', 'Ν.Δ.:', 'Κ.Κ.Ε:', 'ΚΚΕ', 'ΣΥΡΙΖΑ', 'ΔΗΣΥ:', 'ΕΝ. ΚΕΝΤΡΩΩΝ:', 'ΚΕΝΤΡΩΩΝ:', 'Χ.Α:', 'ΔΗ.ΣΥ:', 'ΔΕΣΥ:' 'Α.Π:', 'ΣΥ:', 'ΕΣΠΑ:']
    for speaker in speakers[:]:
        if any(sub in speaker for sub in name_for_delete):
            speakers.remove(speaker)
    speakers = [s.strip() for s in speakers]

   
    for speaker in speakers:
        meta_references = create_meta_references("TLCRole", speaker)
        d.meta.references.append(meta_references)
    
    
    # Discard introductory text before first speaker
    # Use split with maxsplit number 1 in order to split at first occurrence
    try:
        main_text = main_text.split(speakers[0], 1)[1]
    except:
        # prob_files.write(filename + " \n")
        continue  # proceed to next iteration/filename
    print(len(speakers))
    for i in range(len(speakers)):
        if (i % 100 == 0):
            print(i)
        # If not last speaker
        if i < (len(speakers)-1):
            speaker = speakers[i]
            speech, main_text = main_text.split(speakers[i+1], 1)
        else:
            speaker = speakers[i]
            speech = main_text

        # special treatment for first speaker who is usually proedreuon
        if i == 0:
            if proedreuon_first_speaker.search(speaker.strip()):
                speaker = proedreuon_first_speaker.search(
                    speaker.strip()).group()

        # remove parenthesis text which is usually descriptions of procedures
        # speech = re.sub(text_in_parenthesis, " ", speech)
        if (allagi_selidas.search(speaker)):
            speaker = speaker.replace(
                allagi_selidas.search(speaker).group(), '')
            # print(allagi_selidas.search(speaker).group())
        if (allagi_selidas.search(speech)):
            speech = speech.replace(allagi_selidas.search(speech).group(), '')

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
                party = np.nan
                speaker_gender = np.nan
                speaker_region = np.nan
                roles = np.nan
                continue  # to next iteration/speaker

        if speaker.startswith('ΜΑΡΤΥΣ'):
            speaker = speaker.replace('ΜΑΡΤΥΣ', '')
            speaker = re.sub("[()]", '', speaker)
            speaker_info = 'μαρτυς'

            if len(speaker) < 3:  # for cases where the name of the person is not mentioned
                speaker = np.nan
                party = np.nan
                speaker_gender = np.nan
                speaker_region = np.nan
                roles = np.nan
                continue  # to next iteration/speaker

        if general_member_regex.search(speaker):
            speaker = (re.sub("[():'’`΄‘.]", '', speaker))
            speaker = speaker.translate(
                str.maketrans('άέόώήίϊΐiύϋΰ', 'αεοωηιιιιυυυ'))
            if 'εφηβοι' in speaker:
                continue  # to next speaker
            else:
                party = party_of_generic_reference(speaker)
                speaker = np.nan
                speaker_gender = np.nan
                speaker_region = np.nan

                # When the closing speech is assigned to generic members instead of the proedreuon
                # which is usually the case when proedreuon is not mentioned as the closing speaker
                # we remove the standard closing talk of the sitting from the generic members speech

                speaker_info = 'βουλευτης/ες'
                roles = np.nan
                # print("\n\n----------------------\n\n")
                # print("1", [speaker, current_record_datetime.strftime('%d/%m/%Y'),
                #             record_period, record_session, record_sitting,
                #             current_gov, speaker_region, roles, speaker_gender,
                #             speaker_info])
                # print("1eipe:", speech)
                debateSectionParts = create_speeches_akn(
                    speaker=speaker_info, speeches=speech)
                debateSection_main.append(debateSectionParts)
                continue

        # continue
        if speaker != '':
            # Exclude very large malformed text that is not a speaker
            if len(speaker) < 200:
                speaker, speaker_nickname = separate_nickname_incomplete_parenthesis(
                    speaker, speaker_nickname)

                if caps_nickname_in_parenthesis.search(speaker):
                    speaker, speaker_nickname = separate_nickname(speaker)

                if text_in_parenthesis.search(speaker):
                    speaker, speaker_info = separate_explanatory_parenthesis(
                        speaker)
                    speaker_info = format_speaker_info(speaker_info)

                speaker_name = text_formatting(speaker)
                speaker_name = speaker_name_corrections(speaker_name)
                speaker = speaker_name

                # Remove 1-2 letter characters
                speaker_name = ' '.join(
                    [word for word in speaker_name.split(' ') if len(word) > 2])

                max_sim = 0

                for index, row in members_df.iterrows():
                    member_start_date = dt.strptime(
                        row.member_start_date, '%Y-%m-%d')
                    member_end_date = dt.strptime(
                        row.member_end_date, '%Y-%m-%d')

                    if member_start_date <= current_record_datetime <= member_end_date:

                        member_name_part = row.member_name
                        member_party = row.political_party
                        member_region = row.administrative_region
                        member_gender = row.gender
                        member_gov = row.government_name
                        roles = ast.literal_eval(row.roles)

                        temp_max = compute_max_similarity(
                            speaker_name, speaker_nickname, member_name_part)
                        # print([speaker_name,temp_max, member_name_part])

                        if temp_max > max_sim:
                            max_sim = temp_max
                            max_member_name_part = member_name_part
                            max_member_party = member_party
                            max_member_region = member_region
                            max_member_gender = member_gender
                            max_member_roles = roles
                # Strict hand-picked similarity threshold to avoid false positives
                if max_sim > 0.95:
                    max_member_roles = keep_roles_at_date(
                        max_member_roles, current_record_datetime)
                # print("\n\n----------------------\n\n")
                # cm = comment_sto_simio_auto.search(speech)
                # xeir = xeirokrotima.search(speech)
                # if (cm or xeir):
                #     if (cm):
                #         regex_finded = comment_sto_simio_auto
                #         part_splited = 4
                #     elif (xeir):
                #         regex_finded = xeirokrotima
                #         part_splited = 3
                #     splited_text = re.split(regex_finded, speech)
                #     print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                #            record_period, record_session, record_sitting, max_member_party,
                #            current_gov, max_member_region, max_member_roles, max_member_gender,
                #            speaker_info])
                #     print(splited_text[0])
                #     print(
                #         "++++", regex_finded.search(speech).group(), "++++\n")
                #     if (len(splited_text[part_splited]) > 1):
                #         print("+++++")
                #         print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                #                record_period, record_session, record_sitting, max_member_party,
                #                current_gov, max_member_region, max_member_roles, max_member_gender,
                #                speaker_info])
                #         print(splited_text[part_splited])
                # else:
                    # print([speaker_name, max_member_name_part, current_record_datetime.strftime('%d/%m/%Y'),
                    #        record_period, record_session, record_sitting, max_member_party,
                    #        current_gov, max_member_region, max_member_roles, max_member_gender,
                    #        speaker_info])
                    # speaker_name
                    # speech
                debateSectionParts = create_speeches_akn(
                    speaker=speaker_name, speeches=speech)
                debateSection_main.append(debateSectionParts)
                # print("οκ")
            if (ilektroniki_katametrisi_regex.search(speech)):
                print(
                    "++++", ilektroniki_katametrisi_regex.search(speech).group(), "++++\n")
                speech = speech.replace(
                    ilektroniki_katametrisi_regex.search(speech).group(), '')
            # print("3speaker:", speaker_name)
            # print("3eipe:", speech)
            # print("\n\n======================\n\n")
    break

log_file.close()
endtime = dt.now()
print("-----------------")
print(endtime-starttime)
print("-----------------")


xml1 = d.to_xml(encoding='unicode', pretty_print=True)
# print(xml1)

print("-\n\n\n\n\n\n---------------------")


# ---- saving xml to a differnt file
text_file = open("2018__test.xml", "w", encoding='utf8')
n = text_file.write(xml1)
text_file.close()
