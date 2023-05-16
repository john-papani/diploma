from antlr4 import *
from tika import parser
from datetime import datetime as dt
from collections import defaultdict
import re
import os
from bs4 import BeautifulSoup
import sys
sys.path.insert(1, '../antlr4_python')
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser


starttime = dt.now()
record_date = "0000-00-00"
record_period = "00"
record_session = "00"
record_sitting = "00"

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
    global record_date, record_period, record_session, record_sitting
    record_date = date
    record_period = period_detail
    record_session = sunodos
    record_sitting = sunedriasi


datapath = "C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/files/all_files/"

selida_num_regex = re.compile(r"(ΣΕΛΙΔΑ|Σελίδα [0-9]+)")

filenames = sorted([f for f in os.listdir(datapath) if not f.startswith('.')])
print(filenames)
filename_freqs = defaultdict(int)
record_counter = 0
log_file = open('./files_with_problem_16-06-2023.txt', 'a')  


for filename in filenames:
    parsed = parser.from_file(datapath+filename, xmlContent=True)
    record_counter += 1
    if(record_counter%350==0):
        print("File "+str(record_counter)+' from ' +
          str(len(filenames)) + ' '+filename)

    # Skip duplicate files
    # new_name = '_'.join([p for p in filename.split('_') if p!=(filename.split('_')[1])])
    new_name = "_".join([str(record_counter), filename])
    filename_freqs[new_name] += 1
    if filename_freqs[new_name] > 1:
        continue  # with next iteration of for loop
    try:
        content = parsed['content']
        soup = BeautifulSoup(content, 'html.parser')
        f3 = soup.body.get_text()
        f3 = re.sub(selida_num_regex, "", f3)
        split_text = re.split(r"(Αθήνα\,? σήμερα\,?)\s*", f3)
        introduction = split_text[0]
        main_text = split_text[1] + split_text[2]
        set_record_values(introduction)
        # print(record_date)
    except Exception as e:
         log_file.write(f'{filename}: {str(e)}\n')
   
log_file.close()
endtime = dt.now()
print("-----------------")
print(endtime-starttime)
print("-----------------")
