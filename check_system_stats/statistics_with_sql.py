import os
import sqlite3
import traceback 
import xml.etree.ElementTree as ET

conn = sqlite3.connect(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/diploma_dataset_github/raw_text_data/my_harvester_last.db')
cursor = conn.cursor()

def total_files():
    try:
            cursor.execute(
                f"SELECT COUNT(*) AS rowCount FROM debates WHERE fileLocalName IS NOT NULL")
            rows = cursor.fetchall()
            folder_path = "../xml_akn_files/"
            files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
            file_count = len(files)
            print(f"#files_db = {file_count} : #file_xml = {(rows[0][0])} => succeed ==  {round(file_count/rows[0][0]*100,2)}%")

    except Exception as e:
        print(f"An error occurred: {e}")


def starting_files_per_year_in_db():
    try:
        for year in range(1989, 2024):
            cursor.execute(
                f"SELECT fileLocalPath, fileLocalName, debateDate FROM debates WHERE strftime('%Y', datetime(debateDate/1000, 'unixepoch')) = '{year}' AND fileLocalName IS NOT NULL")
            rows = cursor.fetchall()
            print(f"{year} : {len(rows)}")
    except Exception as e:
        print(f"An error occurred: {e}")


def xml_per_year_based_on_db():
    try:
        for year in range(1989, 2024):
            cursor.execute(
                f"SELECT fileLocalPath, fileLocalName, debateDate FROM debates WHERE strftime('%Y', datetime(debateDate/1000, 'unixepoch')) = '{year}' AND fileLocalName IS NOT NULL")
            rows = cursor.fetchall()
            exist = 0
            not_exist = 0
            for row in rows:
                file_path = str("../xml_akn_files/") + \
                    str(row[1]) + str(".xml")
                file_path = file_path.replace("//", "/")
                if os.path.exists(file_path):
                    exist += 1
                else:
                    not_exist += 1
            print(f"{year}: exist= {exist}, not_exist= {not_exist}")
    except Exception as e:
        print(f"An error occurred: {e}")


def speeches_per_year_based_on_xml():
    try:
        for year in range(1989, 2024):
            cursor.execute(
                f"SELECT fileLocalPath, fileLocalName, debateDate FROM debates WHERE strftime('%Y', datetime(debateDate/1000, 'unixepoch')) = '{year}' AND fileLocalName IS NOT NULL")
            rows = cursor.fetchall()
            speeches_per_year = 0
            files_per_year = 0
            for row in rows:
                file_path = str("../xml_akn_files/") + \
                    str(row[1]) + str(".xml")
                file_path = file_path.replace("//", "/")
                if os.path.exists(file_path):
                    # Load the XML file
                    files_per_year += 1
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    akn_namespace = {
                        "akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}
                    debate_section = root.find(
                        './/akn:debateSection[@name="main_debate_section"]', akn_namespace)
                    if debate_section is not None:
                        # Extract information from the parsed XML
                        speech_elems = root.findall(
                            './/akn:speech', akn_namespace)

                        # Get the last <div> element
                        last_speech = speech_elems[-1]
                        # Get the 'eid' attribute of the last <div> element
                        eid = last_speech.get('eId')
                        if eid is not None:
                            speeches_per_year += int(eid.split("_")[-1])
                    else:
                        print("No <div> elements found in the XML.")
            if (files_per_year != 0):
                print(f"{year}: #Total speeches={speeches_per_year} ~ Average_speeches_per_file={round(speeches_per_year/files_per_year)} ~ Files={files_per_year}")
    except Exception as e:
        print(f"An error occurred: {e}")


def files_per_period():
    try:
        cursor.execute(
            "SELECT debatePeriod, count(fileLocalName) FROM debates WHERE fileLocalName IS NOT NULL GROUP BY debatePeriod ORDER by debatePeriod")
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute(
                f'SELECT fileLocalPath, fileLocalName FROM debates WHERE debatePeriod = "{row[0]}"')
            rows_ = cursor.fetchall()
            # print(rows_)
            exist = 0
            not_exist = 0

            for row_ in rows_:
                file_path = str("../xml_akn_files/") + \
                    str(row_[1]) + str(".xml")
                file_path = file_path.replace("//", "/")
                if os.path.exists(file_path):
                    exist += 1
                else:
                    not_exist += 1
            print(f"{row[0]}: exist= {exist}, not_exist= {not_exist}")
            # print(f"{row[0]}, {exist}, {not_exist}")

      
    except Exception as e:
        print(f"An error occurred: {traceback.format_exc()}")

total_files()
print("\n\n------------------------\n\n")
starting_files_per_year_in_db()
print("\n\n------------------------\n\n")
xml_per_year_based_on_db()
print("\n\n------------------------\n\n")
speeches_per_year_based_on_xml()
print("\n\n------------------------\n\n")
files_per_period()



conn.close()


