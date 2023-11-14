
import csv
from datetime import datetime as dt
import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

starttime = dt.now()

new_json_file = "../json_files/parties_with_wikitada.json"

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


def create_json_parties():
    parties_json = "../json_files/parties.json"

    with open('../useful_csv_for_parl_members/_parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv', 'r', encoding='utf8') as file_csv:
        csv_data = (csv.reader(file_csv))
        next(csv_data, None)
        for index, row in enumerate(csv_data):
            party = convert_greek_to_english(row[3])
            add_to_json(party, "empty", parties_json)


def add_to_json(name_speaker, wiki_link, jsonfile):
    with open(jsonfile, 'r', encoding='utf8') as file:
        data = json.load(file)
    if wiki_link == "empty":
        data[name_speaker] = ""
    else:
        data[name_speaker] = wiki_link

    # Save the updated JSON data to the file
    with open(jsonfile, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def search_for_wikidata_connection(name):

    if (name == "suriza_-_proodeutiki_summaxia"):
        name = "syriza"
    elif (name == "laikos_sundesmos_-_xrusi_augi"):
        name = "xrusi_augi"
    elif (name == "anexartitoi_dimokratikoi_bouleutes"):
        return "https://www.wikidata.org/wiki/Q16737351"
    elif (name == "dimokratiko_koinoniko_kinima"):
        return "https://www.wikidata.org/wiki/Q1226100"
    elif (name == "dimokratiki_sumparataxi_(panellinio_sosialistiko_kinima_-_dimokratiki_aristera)"):
        return "https://www.wikidata.org/wiki/Q21075797"
    elif (name == "elliniki_lusi_-_kuriakos_belopoulos"):
        return "https://www.wikidata.org/wiki/Q50736163"
    elif (name == "anexartitoi_ellines_ethniki_patriotiki_dimokratiki_summaxia"):
        return "https://www.wikidata.org/wiki/Q529666"
    elif (name == "oikologoi_enallaktikoi_(omospondia_oikologikon_enallaktikon_organoseon)"):
        return "https://www.wikidata.org/wiki/Q3563454" 
    elif (name == "enosi_kentroon"):
        return "https://www.wikidata.org/wiki/Q3567209"
    elif (name == "dimokratiko_patriotiko_kinima_niki"):
        return "https://www.wikidata.org/wiki/Q118559247"
    elif (name =="sunaspismos_tis_aristeras_ton_kinimaton_kai_tis_oikologias"):
        return "https://www.wikidata.org/wiki/Q219573"
    elif (name == "anexartitoi_(ektos_kommatos)"):
        return -1

    name = name.replace("_", " ")

    # Initialize the WebDriver
    # options = webdriver.EdgeOptions()
    driver = webdriver.Edge()

    url_google = "https://www.google.com/search?q="
    search_query = f"{name} party wikidata"
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
            return result_link
            # return -1


def create_json_with_wikidata_parties():

    parties_from_json = open(
        '../json_files/parties.json', 'r', encoding='utf8')
    parties = json.load(parties_from_json)
    try:
        for party in parties:
            wiki_link = search_for_wikidata_connection(party)
            if (wiki_link != -1 and wiki_link != None):
                add_to_json(party, wiki_link, new_json_file)
            else:
                print(party)

    finally:
        end = dt.now()
        print(end-starttime)
        # new_json_file.close()


create_json_parties()
print("====")
create_json_with_wikidata_parties()
print("OK")
