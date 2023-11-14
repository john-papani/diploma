
import csv
import requests
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime as dt
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

starttime = dt.now()

new_json_file = "./parties_with_wikitada.json"
log_file = open('./tenure_wikidata_problems.txt', 'a', encoding="utf8")


def add_to_json(name_speaker, wiki_link):
    with open(new_json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    data[name_speaker] = wiki_link
    # Save the updated JSON data to the file
    with open(new_json_file, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def remove_diacritics(text):
    return unidecode(text)


# URL of the Wikipedia page to search on
wiki_url = "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%AC%CE%BB%CE%BF%CE%B3%CE%BF%CF%82_%CF%85%CF%80%CE%BF%CF%85%CF%81%CE%B3%CE%B5%CE%AF%CF%89%CE%BD_%CF%84%CE%B7%CF%82_%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%BA%CF%85%CE%B2%CE%AD%CF%81%CE%BD%CE%B7%CF%83%CE%B7%CF%82"

def add_to_json_upourgoi(value, json_file):
    # Load existing data from JSON file
    with open(json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    # Check if the name exists in the JSON data
    if value not in data:
        data[value] = {}

        without_property = value.replace("υφυπουργος", "").replace(
            "υπουργος", "").replace("αναπληρωτης", "").strip()

        sub_value = {
            "without_property": without_property,
            "wiki_link": ""
        }
        data[value].update(sub_value)
        with open(json_file, 'w', encoding='utf8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def create_json_with_tenures():
    upourgoi = "../json_files/upourgoi.json"
    with open('../useful_csv_for_parl_members/_formatted_roles_gov_members_data_11_2023.csv', 'r', encoding='utf8') as file_csv:
        csv_data = (csv.reader(file_csv))
        next(csv_data, None)
        for index, row in enumerate(csv_data):
            role = row[1]
            add_to_json_upourgoi(role, upourgoi)


def get_wikidata_link(wikipedia_link, driverEdge):
    driverEdge.get(wikipedia_link)
    try:
        option = driverEdge.find_element(By.ID, "t-wikibase")
        a_element = option.find_element(By.TAG_NAME, "a")
        href = a_element.get_attribute("href")
        response = requests.head(href, allow_redirects=True)
        final_url = response.url
        print(f"Link Href for {wikipedia_link}: {final_url}")
        if final_url.startswith("https://www.wikidata.org/wiki/Q"):
            return final_url
        else:
            return final_url
            # return -1

    except Exception as e:
        return wikipedia_link


def get_wikipedia_link(ident_without_prop, driver, driverEdge):
    driver.get(wiki_url)
    found = False
    wikipedia_link = ""

    # Find all links on the page
    links = driver.find_elements(By.XPATH, "//a")
    # Search with the original search string (with diacritics)
    try:
        for link in links:
            link_text = link.text
            if ident_without_prop in link_text:
                found = True
                wikipedia_link = link.get_attribute("href")
                break
        # If not found, search with the normalized search string (without diacritics)
        if not found:
            ident_without_prop_normalized = remove_diacritics(
                ident_without_prop)
            for link in links:
                link_text = link.text
                link_text_normalized = remove_diacritics(link_text)
                link_text_normalized = link_text_normalized.replace(
                    ",", "")
                if ident_without_prop_normalized.lower() in link_text_normalized.lower():
                    found = True
                    wikipedia_link = link.get_attribute("href")
                    break
        print(wikipedia_link)
        if (wikipedia_link.startswith("https://el.wikipedia.org/w/index.php")):
            log_file.write(f'{ident_without_prop}\n')
            return None
        wikidata_ = get_wikidata_link(wikipedia_link, driverEdge)
        return wikidata_
    except Exception as e:
        log_file.write(f'{ident_without_prop}\n')
        print(wikipedia_link, e)


def create_json_with_wikidata_tenure():
    driver = webdriver.Chrome()
    driver2 = webdriver.Edge()
    upourgoi_with_wikidata = "../json_files/upourgoi_with_wikidata.json"
    upourgoi = "../json_files/upourgoi.json"
    upourgoi_file = open(
        upourgoi, 'r', encoding='utf8')
    data = json.load(upourgoi_file)
    try:
        for key, value in data.items():
            if value['without_property'] == "βιομηχανιας ενεργειας και τεχνολογιας":
                wiki_link = "https://www.wikidata.org/wiki/Q121009910"
            elif value['without_property'] == "παιδειας θρησκευματων πολιτισμου και αθλητισμου":
                wiki_link = "https://www.wikidata.org/wiki/Q20679949"
            elif value['without_property'] == "οικονομιας και αναπτυξης":
                wiki_link = "https://www.wikidata.org/wiki/Q31284082"
            elif value['without_property'] == "εργασιας κοινωνικης ασφαλισης και κοινωνικης αλληλεγγυης":
                wiki_link = "https://el.wikipedia.org/wiki/%CE%A5%CF%80%CE%BF%CF%85%CF%81%CE%B3%CE%B5%CE%AF%CE%BF_%CE%95%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82,_%CE%9A%CE%BF%CE%B9%CE%BD%CF%89%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%91%CF%83%CF%86%CE%AC%CE%BB%CE%B9%CF%83%CE%B7%CF%82_%CE%BA%CE%B1%CE%B9_%CE%9A%CE%BF%CE%B9%CE%BD%CF%89%CE%BD%CE%B9%CE%BA%CE%AE%CF%82_%CE%91%CE%BB%CE%BB%CE%B7%CE%BB%CE%B5%CE%B3%CE%B3%CF%8D%CE%B7%CF%82"
            elif value['without_property'] == "εργασιας και κοινωνικης αλληλεγγυης":
                wiki_link = "https://www.wikidata.org/wiki/Q65273449"
            elif value['without_property'] == "εργασιας και κοινωνικων υποθεσεων":
                wiki_link = "https://www.wikidata.org/wiki/Q65273449"
            elif value['without_property'] == "οικονομιας αναπτυξης και τουρισμου":
                wiki_link = "https://www.wikidata.org/wiki/Q21029361"
            elif value['without_property'] == "πολιτισμου":
                wiki_link = "https://www.wikidata.org/wiki/Q16331895"
            elif value['without_property'] =="κοινωνικης συνοχης και οικογενειας":
                wiki_link = "https://www.wikidata.org/wiki/Q120084687"
            elif value['without_property'] =="παιδειας θρησκευματων και αθλητισμου":
                wiki_link = "https://www.wikidata.org/wiki/Q16331885"
            else:
                wiki_link = get_wikipedia_link(
                    value['without_property'], driver, driver2)
            if key in data and wiki_link != None:
                print(str(wiki_link))
                data[key]["wiki_link"] = str(wiki_link)

                with open(upourgoi_with_wikidata, 'w', encoding='utf8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
    finally:
        driver.close()
        driver2.close()
        log_file.close()
        end = dt.now()
        print(end-starttime)

create_json_with_tenures()
create_json_with_wikidata_tenure()
print("OKKK")
