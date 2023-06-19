from antlr4 import *
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser

# class MyListener(ParseTreeListener):
#     def enterTable_of_contents(self, ctx):
#         toc = []
#         for child in ctx.getChildren():
#             toc.append(child.getText())
#         print("Table of Contents: ", ", ".join(toc))


def get_subjects(tree_subjects):
    if tree_subjects:
        for section in tree_subjects.sectionContent():
            if section.sbcategory() and section.sbcategory().SUBJECT_BASIC_CATEGORY():
                print(
                    "--", section.sbcategory().SUBJECT_BASIC_CATEGORY().getText(), "--")
            for sub in section.subject():
                print(sub.SUBJECT_().getText())
    else:
        print("There are no subjects")


def get_proedreuontes(tree_proedreuontes):
    flag_no_proedros = True
    if tree_proedreuontes:
        print("111")
        for proedreuontes in tree_proedreuontes.proedreuontes():
            flag_no_proedros = False
            if (proedreuontes.PROEDREUONTES()):
                print("--", proedreuontes.PROEDREUONTES().getText(), "--")
            for proedreuontes_name in proedreuontes.proedreuontes_name():
                print(proedreuontes_name.NAME().getText())
    if flag_no_proedros or (not tree_proedreuontes):
        print("There are no PROEDREUONTES")


def get_all_speakers(tree_speakers):
    if (tree_speakers):
        for speakers in tree_speakers.speaker_detail():
            if (speakers.SPEAKER_CATEG_DETAIL()):
                print("--", speakers.SPEAKER_CATEG_DETAIL().getText(), "--")
            for speaker in speakers.speakers_name():
                speaker_name = speaker.NAME().getText()
                speaker_name = speaker_name.replace(" , σελ.", "")
                print(speaker_name)
    else:
        print("There are not SPEAKERS")


# def get_text_or_none(child):
#     if child is not None:
#         if isinstance(child, list):
#             return [get_text_or_none(sub_child) for sub_child in child]
#         else:
#             return child.getText()
#     else:
#         return None


def take_toc(tree):
    tree_toc = tree.table_of_contents()
    get_text_or_none = lambda child: [get_text_or_none(sub_child) if isinstance(sub_child, list) else (sub_child.getText() if sub_child is not None else None) for sub_child in child] if isinstance(child, list) else (child.getText() if child is not None else None)
    if tree_toc:
          # Extract parliament details
        anatheoritiki_bouli = get_text_or_none(tree_toc.anatheoritiki_bouli())
        period_detail = get_text_or_none(tree_toc.period_detail())
        dimokratia = get_text_or_none(tree_toc.dimokratia())
        sunodos = get_text_or_none(tree_toc.sunodos())
        ergasies = get_text_or_none(tree_toc.ergasies())
        sunedriasi = get_text_or_none(tree_toc.sunedriasi())
        date = get_text_or_none(tree_toc.date())
        print(date)


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
    tree_proedreuontes = tree.proedreuontes()
    tree_speakers = tree.speakers()
    tree_parlDetails = tree.parliament_proceedings().parliament_detail()
    print(tree_parlDetails)
    print("\n\n-------------------------\n\n")

    # Extract parliament details
    # anatheoritiki_bouli = tree_parlDetails.anatheoritiki_bouli().getText(
    # ) if tree_parlDetails.anatheoritiki_bouli() is not None else None
    # period_detail = tree_parlDetails.period_detail().getText(
    # ) if tree_parlDetails.period_detail() is not None else None
    # dimokratia = tree_parlDetails.dimokratia().getText(
    # ) if tree_parlDetails.dimokratia() is not None else None
    # sunodos = tree_parlDetails.sunodos().getText(
    # ) if tree_parlDetails.sunodos() is not None else None
    # ergasies = tree_parlDetails.ergasies().getText(
    # ) if tree_parlDetails.ergasies() is not None else None
    # sunedriasi = tree_parlDetails.sunedriasi().getText(
    # ) if tree_parlDetails.sunedriasi() is not None else None
    # date = tree_parlDetails.date().getText(
    # ) if tree_parlDetails.date() is not None else None

    # # Print out the extracted details
    # print(f"Anatheoritiki bouli: {anatheoritiki_bouli}")
    # print(f"Period detail: {period_detail}")
    # print(f"Dimokratia: {dimokratia}")
    # print(f"Sunodos: {sunodos}")
    # print(f"Ergasies: {ergasies}")
    # print(f"Sunedriasi: {sunedriasi}")
    # print(f"Date: {date}")

    # print("\n\n-------------------------\n\n")
    # all_subjects = get_subjects(tree_subjects)
    # print("\n\n-------------------------\n\n")
    # get_proedreuontes(tree)
    # print("\n\n-------------------------\n\n")
    # get_all_speakers(tree_speakers)
    take_toc(tree=tree)

    # listener = MyListener()
    # ParseTreeWalker.DEFAULT.walk(listener, tree)


if __name__ == '__main__':
    main()
