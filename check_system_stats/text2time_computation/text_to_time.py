import csv
from datetime import datetime, timedelta
import os
import sqlite3
import traceback
import xml.etree.ElementTree as ET
from rdflib import Namespace, Literal, URIRef, Graph
import json


starttime = datetime.now()
akn_namespace = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}


# Define the xml files
datapath = "C:/Users/johnp/Documents/ECE_NTUA/diploma/diploma_github/xml_akn_files/"


conn = sqlite3.connect(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/diploma_dataset_github/raw_text_data/my_harvester_last.db')
cursor = conn.cursor()


sql_query = """
    SELECT 
        fileLocalName
    FROM debates
    WHERE strftime('%Y-%m-%d', datetime(debateDate/1000, 'unixepoch', '+3 hours')) = ?
        AND filelocalName IS NOT NULL
"""

# Lists of values
formatted_date_str_list = []
total_time_list = []
try:
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2023, 1, 1)
    # Loop through the date range
    current_date = start_date
    while current_date <= end_date:
        formatted_date_str = current_date.strftime('%Y-%m-%d')
        print(formatted_date_str)
        cursor.execute(sql_query, (formatted_date_str,))
        results = cursor.fetchall()
        # Move to the next date
        current_date += timedelta(days=1)
        # Initialize counters per day
        total_time_per_day = 0
        speeches_per_day = 0
        for index, filename in enumerate(results):
            filename = filename[0]
            # print(filename)
            # Parse the XML from a file
            xml_file_path = datapath+filename+".xml"
            if os.path.exists(xml_file_path):
                tree = ET.parse(xml_file_path)
                # Get the root element of the XML tree
                root = tree.getroot()
                # Find the debate section element with name="main_debate_section"
                debate_section = root.find(
                    './/akn:debateSection[@name="main_debate_section"]', akn_namespace)
                # Check if the debate section exists
                if debate_section is not None:
                    # Extract information from the parsed XML
                    speech_elems = root.findall('.//akn:speech', akn_namespace)
                    for speech_elem in speech_elems:
                        length_speech_elems = len(speech_elems)
                        speech_by = speech_elem.attrib['by']
                        name_speaker = speech_elem.find(
                            './/akn:from', akn_namespace).text
                        spoken_text_elems = speech_elem.findall(
                            './/akn:p', akn_namespace)
                        spoken_text = '\n'.join(
                            [elem.text for elem in spoken_text_elems if elem.text is not None])
                        words_in_speech = len(spoken_text.split())
                        time_speech = (words_in_speech/130)*60  # in seconds
                        speeches_per_day += 1
                        total_time_per_day += time_speech
            else:
                print(f"File not found: {xml_file_path}")
        average_time_per_speech = int(
            total_time_per_day/speeches_per_day) if speeches_per_day > 0 else 0
        # Append to the lists
        # if speeches_per_day > 0:
        formatted_date_str_list.append(formatted_date_str)
        total_time_list.append(average_time_per_speech)

except Exception as e:
    print(f"An error occurred: {traceback.format_exc()}")


# Specify the CSV file path
csv_file_path = './output.csv'
# Write data to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(['Date', 'Average Time (seconds) per Speech'])
    # Write data
    for data in zip(formatted_date_str_list, total_time_list):
        csv_writer.writerow(data)
print(f"CSV file '{csv_file_path}' created successfully.")


endtime = datetime.now()
print("-----------------")
print(endtime-starttime)
print("-----------------")
