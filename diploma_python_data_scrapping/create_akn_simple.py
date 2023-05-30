


from cobalt import Act, AmendmentEvent, Debate, DebateStructure, schemas
from cobalt.akn import StructuredDocument
from cobalt.akn import get_maker
# from lxml.builder import E
from lxml import etree as ET, objectify

from lxml.builder import ElementMaker  # lxml only !

from antlr4 import *
import sys
sys.path.insert(1, './antlr4_python')
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser
E = ElementMaker(nsmap={None: 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'},
                 namespace='http://docs.oasis-open.org/legaldocml/ns/akn/3.0')


papa = "Asdd"

speakers = ["ΓΙΑΝΝΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ", "ΜΆΡΙΟΣ ΚΌΝΙΑΡΗΣ", "c", "d"]
speeches = "In this updated version, the convert_greek_to_english function first splits the input Greek\nsentence into individual words using the split() method. It then iterates over each word and converts it to English using the same logic as before.\nThe converted words are stored in a list. Finally, the '_'.join() method is used to join the converted words with underscores in between.\nThe example usage demonstrates how to convert a Greek sentence and print the resulting English words separated by underscores"


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
    'υ': 'y',
    'φ': 'f',
    'χ': 'x',
    'ψ': 'ps',
    'ω': 'o',
}


def convert_greek_to_english(whole_name):
    words = whole_name.split()
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


def create_themata_preface_akn(tree_subjects):
    themata_section = E.section(name="subjects")
    all_subjects = []
    if tree_subjects:
        for section in tree_subjects.sectionContent():
            if section.sbcategory() and section.sbcategory().SUBJECT_BASIC_CATEGORY():
                categ_name = E.heading(
                    section.sbcategory().SUBJECT_BASIC_CATEGORY().getText())
                all_subjects.append(categ_name)
            for sub in section.subject():
                subject_text = sub.SUBJECT_().getText()
                subject_text = E.p(subject_text)
                all_subjects.append(subject_text)
    themata_section.extend(all_subjects)
    return themata_section


def create_speakers_preface_akn(tree_speakers):
    speakers_section = E.section(name="speakers")
    all_speakers = []
    if (tree_speakers):
        for speakers in tree_speakers.speaker_detail():
            if (speakers.SPEAKER_CATEG_DETAIL()):
                categ_name = E.heading(
                    speakers.SPEAKER_CATEG_DETAIL().getText())
                all_speakers.append(categ_name)
            for speaker in speakers.speakers_name():
                speaker_name = speaker.NAME().getText()
                speaker_name = speaker_name.replace(" , σελ.", "")
                speaker_name_ = E.p(speaker_name)
                all_speakers.append(speaker_name_)
    speakers_section.extend(all_speakers)
    return speakers_section


def create_preface_akn():
    preface = E.preface()
    # themata = create_themata_preface_akn()
    # debate.preface.append(themata)
    # simiosi
    # table_of_content
    # themata
    # proedros
    # speakers
    # basic_parliament_proceedings

    return preface


d = Debate()
# d.meta.notes = "TESTING FILE HERE"
# print(d.non_eid_portions)
d.expression_date = "2015-01-02"
d.manifestation_date = "2030-10-01"
d.manifestation_format = "xml"
d.refs = "222222"
d.frbr_uri = "/akn/gr-ath/debate/2015-01-10/1/"
d.frbr_uri.work_componenent = ""
d.language = "gr"
d.title = "ΔΙΑΛΟΓΟΣ 55A 2015/01/02"


# ----- meta references ---
# d.meta.references.attrib.pop("source")  # remove attribute
d.meta.references.TLCOrganization.attrib["eId"] = "greek_parl"
d.meta.references.TLCOrganization.attrib["href"] = "/ontology/organization/akn/greek_parl"
d.meta.references.TLCOrganization.attrib["showAs"] = "Greek_Parliament"

TLCRole1 = d.make_element("TLCRole", attribs={
    "eId": "proedros", "href": "/ontology/person/akn/parliament/proedros", "showAs": "PROEDROS"})
# TLCRole1.set("eId","MAGKAS") -- kai auto doyleuei
d.meta.references.append(TLCRole1)
TLCPerson = d.make_element("TLCPerson", attribs={
    "eId": "giannis_papanikolaou", "href": "/ontology/person/akn/parliament/giannis_papanikolaou", "showAs": "Giannis Papanikolaou"})
d.meta.references.append(TLCPerson)


# ----- main text ---
# section.p.attrib["eId"] = ""

# speech1 = d.make_element("speech", attribs={
#     "from": "nikos", "eId": "1"})

# speech1.set('text', "ela aleko")
# speech2 = d.make_element("speech", attribs={
#     "from": "giannis", "eId": "2"})
# speech3 = d.make_element("speech", attribs={
#     "from": "marios", "eId": "3", 'text': "EIMAI MEGALOS MALAKAS"})
# debateSection1 = d.make_element("debateSection", attribs={
#     "eid": "1014"})
# pa1 = d.make_element("p")
# pa2 = d.make_element("p")
# pa3 = d.make_element("p")


from1 = d.make_element("from")

# speech.attrib["from"] = "assssssssd"
# speech.attrib["text"] = "text speech"
# d.debateBody.attrib["eId"] = "pappap"

# # # d.get_element("d.debateBody.debateSection.speech1", root=section)

# # print(type(speech2))
# # speech2.append(pa)
# # print(speech2.get("eId"))
# # print(speech2.body.text)
# # speech2.append(from1)
main_text = "Αθήνα, σήμερα στις 25 Ιανουαρίου 2018, ημέρα Πέμπτη και ώρα 9.35΄, συνήλθε στην Αίθουσα της Γερουσίας η Βουλή σε ολομέλεια για να συνεδριάσει υπό την προεδρία του Β΄ Αντιπροέδρου αυτής κ. ΓΕΩΡΓΙΟΥ ΒΑΡΕΜΕΝΟΥ.\nΠΡΟΕΔΡΕΥΩΝ (Γεώργιος Βαρεμένος): Κυρίες και κύριοι συνάδελφοι, αρχίζει η συνεδρίαση."
debateSection_preamble = create_preamble_akn(
    main_text.split('\n', 1)[0], name="opening")
d.main_content.append(debateSection_preamble)
debateSection = create_debateSection_akn()
d.main_content.append(debateSection)


with open('./antlr4_python/debate.txt', 'r', encoding='utf-8') as f:
    input_str = f.read()

input_stream = InputStream(input_str)
lexer = DebateGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = DebateGrammarParser(token_stream)

tree = parser.start()
# print(tree.toStringTree())
preface1 = create_preface_akn()
# d.main_content.append(preface1)

subjects = create_themata_preface_akn(tree.subjects())
speakers = create_speakers_preface_akn(tree.speakers())
# preface1.append(subjects)
# preface1.append(speakers)

# for i in range(len(speakers)):
#     debateSectionParts = create_speeches_akn(
#         speaker=speakers[i], speeches=speeches)
#     debateSection.append(debateSectionParts)
# debateSection.append(debateSectionParts)
# speech1.append(pa1)
# print("debateScriotn =", type(debateSection1))
# debateSection1.append(speech1)

# speech2.append(pa2)


# debateSection1.append(speech2)
# speech3.append(pa3)
# debateSection1.append(speech3)
# #  d.debateBody.make_element(speech1)
# child = d.debateBody.debateSection.speech[0]['p']

# d.debateBody.debateSection.speech[1].__setitem__('p',"KAPOS")
# d.debateBody.debateSection.speech[2].__setitem__('p',"MAGIKS")
# # print(speech3.set('text', "Xeirokrotima"))
# # print(speech3.text)
# # print(d.work_date)
# d.debateBody.debateSection['p'].attrib.pop('eId')
# print(d.debateBody.debateSection.speech[1].set("tesxt","asdsd"))
# print(d.debateBody.descendantpaths())



# print(d.meta.addnext(preface1))

# print(d.debateBody.debateSection.descendantpaths())

# print(xml1)
for i in d.debateBody.descendantpaths():
    print(i)

d.debateBody.remove(d.debateBody.debateSection[0])
for i in d.debateBody.descendantpaths():
    print(i)

xml1 = d.to_xml(encoding='unicode', pretty_print=True)
print("-\n\n\n\n\n\n---------------------")

# ---- saving xml to a differnt file
text_file = open("akoma_ntoso_mock.xml", "w", encoding='utf8')
n = text_file.write(xml1)
text_file.close()
