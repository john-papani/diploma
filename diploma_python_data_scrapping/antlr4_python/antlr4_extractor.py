from antlr4 import *
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser


def praktika_boulis_details(parlDetails):
    anatheoritiki_bouli = parlDetails.anatheoritiki_bouli().getText(
    ) if parlDetails.anatheoritiki_bouli() is not None else None
    period_detail = parlDetails.period_detail().getText(
    ) if parlDetails.period_detail() is not None else None
    dimokratia = parlDetails.dimokratia().getText(
    ) if parlDetails.dimokratia() is not None else None
    sunodos = parlDetails.sunodos().getText(
    ) if parlDetails.sunodos() is not None else None
    ergasies = parlDetails.ergasies().getText(
    ) if parlDetails.ergasies() is not None else None
    sunedriasi = parlDetails.sunedriasi().getText(
    ) if parlDetails.sunedriasi() is not None else None
    date = parlDetails.date().getText() if parlDetails.date() is not None else None

    # Print out the extracted details.
    print(f"Anatheoritiki bouli: {anatheoritiki_bouli}")
    print(f"Period detail: {period_detail}")
    print(f"Dimokratia: {dimokratia}")
    print(f"Sunodos: {sunodos}")
    print(f"Ergasies: {ergasies}")
    print(f"Sunedriasi: {sunedriasi}")
    print(f"Date: {date}")


def print_subjects(tree_subjects):
    for subject_category in tree_subjects.subjects_category():
        for subject in subject_category.subject():
            subject_text = subject.SUBJECT_().getText()
            print("---!----")
            subject_text = subject_text.replace(" , σελ.", "")
            print(subject_text)

def print_all_speakers(tree_speakers):
     for speakers in tree_speakers.speaker_detail():
        for speaker in speakers.speakers_name():
            speaker_name = speaker.NAME().getText()
            speaker_name = speaker_name.replace(" , σελ.", "")
            print(speaker_name)
def main():

    # read the input from a text file
    with open('debate.txt', 'r', encoding='utf-8') as f:
        input_str = f.read()

    input_stream = InputStream(input_str)
    lexer = DebateGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DebateGrammarParser(token_stream)

    tree = parser.start()
    # print(tree.toStringTree())

    tree_subjects = tree.subjects()
    tree_speakers = tree.speakers()

    parlDetails = tree.parliament_proceedings().parliament_detail()
    print("\n\n-------------------------\n\n")
    praktika_boulis_details(parlDetails)
    print("\n\n-------------------------\n\n")
    print_subjects(tree_subjects)
    print("\n\n-------------------------\n\n")
    print_all_speakers(tree_speakers)

if __name__ == '__main__':
    main()
