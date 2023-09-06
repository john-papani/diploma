
import csv
from datetime import datetime as dt
import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

starttime = dt.now()

new_json_file = "./names_with_wikidata.json"


def add_to_json(name_speaker, wiki_link):
    with open(new_json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    data[name_speaker] = wiki_link
    # Save the updated JSON data to the file
    with open(new_json_file, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def search_for_wikidata_connection(name):

    name = name.replace("_", " ")
    # Initialize the WebDriver
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)

    url_google = "https://www.google.com/search?q="
    search_query = f"{name} wikidata"
    driver.get(url_google + search_query)
    time.sleep(1)
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    if search_results:
        first_result = search_results[0]
        link_element = first_result.find_element(By.CSS_SELECTOR, "a")
        result_link = link_element.get_attribute("href")

        # Close the WebDriver
        driver.close()
        # Check if the link starts with "www.wikidata.org/"
        if result_link.startswith("https://www.wikidata.org/wiki/Q"):
            return result_link
        else:
            return -1


def create_rdf_members_with_details():
    file_speakers_from_xmls = open(
        '../all_speakers_names.json', 'r', encoding='utf8')
    speakers_from_xmls = json.load(file_speakers_from_xmls)

    file_speakers_from_official = open(
        '../official_data_directory.json', 'r', encoding='utf8')
    speakers_from_official = json.load(file_speakers_from_official)
    try:
        with open('../useful_csv_for_parl_members/_parl_members_activity_1989onwards_with_gender.csv', 'r', encoding='utf8') as file_csv:
            csv_data = (csv.reader(file_csv))
            next(csv_data, None)
            for name_speaker in speakers_from_xmls:
                wiki_link = search_for_wikidata_connection(name_speaker)
                if name_speaker in speakers_from_official:
                    # Reset the file pointer to the beginning
                    file_csv.seek(0)
                    next(csv_data, None)
                    for row in csv_data:
                        if str(row[6]) == str(name_speaker):
                            gender = row[5]
                            if (wiki_link != -1 and wiki_link != None):
                                add_to_json(name_speaker, wiki_link)
                            break
                else:

                    if (wiki_link != -1 and wiki_link != None):
                        add_to_json(name_speaker, wiki_link)

    finally:
        end = dt.now()
        print(end-starttime)
        new_json_file.close()


create_rdf_members_with_details()
