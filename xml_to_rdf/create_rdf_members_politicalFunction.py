import csv
from datetime import datetime as dt
import datetime
import rdflib
from rdflib import Namespace, Literal, URIRef
import json

starttime = dt.now()

dcterms = Namespace("http://purl.org/dc/terms/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
greek_lp = Namespace(
    "https://purl.org/greekparldebates/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
foaf = Namespace("http://xmlns.com/foaf/0.1/")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
owl = Namespace('http://www.w3.org/2002/07/owl#')
schema = Namespace('https://schema.org/')

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

added_names = set()


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


def add_column_to_csv(input_file, output_file, num):
    with open(input_file, 'r', encoding='utf8') as f_in, open(output_file, 'w', newline='', encoding='utf8') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        # Read the header row
        header = next(reader)

        # Add the new column header to the header row
        new_column_header = "name"
        header.append(new_column_header)

        # Write the updated header row to the output file
        writer.writerow(header)

        # Iterate over each row in the input file
        for row in reader:
            # Generate the new column value based on existing columns
            if num == 1:
                new_column_value = "_".join(
                    [row[0].split(" ")[0], row[0].split(" ")[1]])
            else:
                new_column_value = "_".join(
                    [row[0].split(" ")[2], row[0].split(" ")[0]])
            new_column_value = convert_greek_to_english(new_column_value)
            # Append the new column value to the row
            row.append(new_column_value)

            # Write the updated row to the output file
            writer.writerow(row)


def create_json_official_parl_mem():
    official_parl_file = open(
        "./useful_csv_for_parl_members/_parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv", 'r', encoding='utf8')
    reader = csv.reader(official_parl_file)
    next(reader, None)
    json_file = "./official_data_directory.json"
    with open(json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
        speaker_id = len(data)
    for row in reader:
        if len(row) >= 3:
            name = "_".join([row[0].split(" ")[2], row[0].split(" ")[0]])
            name_ = convert_greek_to_english(name)
            if name_ not in data:
                speaker_id += 1
                added_names.add(name_)
                data[convert_greek_to_english(name)] = speaker_id
                with open(json_file, 'w', encoding='utf8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
    file.close()
    official_parl_file.close()


def create_rdf_members_with_details():
    g_speakers_with_party = rdflib.Graph()
    g_speakers_with_party.bind("greek_lp", greek_lp)

    file_speakers_from_xmls = open(
        './all_speakers_names.json', 'r', encoding='utf8')
    speakers_from_xmls = json.load(file_speakers_from_xmls)
    names_wikidata = open(
        './wikidata_crawler/names_with_wikidata.json', 'r', encoding='utf8')
    names_wikidata_json = json.load(names_wikidata)
    file_speakers_from_official = open(
        './official_data_directory.json', 'r', encoding='utf8')
    speakers_from_official = json.load(file_speakers_from_official)
    try:
        with open('./useful_csv_for_parl_members/_parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv', 'r', encoding='utf8') as file_csv:
            csv_data = (csv.reader(file_csv))
            next(csv_data, None)
            for name_speaker in speakers_from_xmls:
                if name_speaker in speakers_from_official:
                    # Reset the file pointer to the beginning
                    file_csv.seek(0)
                    next(csv_data, None)
                    for row in csv_data:
                        if str(row[6]) == str(name_speaker):
                            gender = row[5]
                            subject = URIRef(
                                greek_lp[f"GRmember_{speakers_from_xmls[name_speaker]}"])
                            g_speakers_with_party.add(
                                (subject, foaf.name, Literal(name_speaker)))
                            g_speakers_with_party.add(
                                (subject, foaf.gender, Literal(gender)))
                            if name_speaker in names_wikidata_json:
                                g_speakers_with_party.add(
                                    (subject, owl.sameAs, URIRef(names_wikidata_json[name_speaker])))
                            break
                else:
                    subject = URIRef(
                        greek_lp[f"GRmember_{speakers_from_xmls[name_speaker]}"])
                    g_speakers_with_party.add(
                        (subject, foaf.name, Literal(name_speaker)))
                    if name_speaker in names_wikidata_json:
                        g_speakers_with_party.add(
                            (subject, owl.sameAs, URIRef(names_wikidata_json[name_speaker])))
    finally:
        with open(f"./rdfs/rdf_speakers.rdf", "w", encoding='utf8') as f:
            f.write(g_speakers_with_party.serialize(format='xml'))

    f.close()
    file_csv.close()
    file_speakers_from_official.close()
    file_speakers_from_xmls.close()

def add_to_json(value, json_file):
    # Load existing data from JSON file
    with open(json_file, 'r', encoding='utf8') as file:
        data = json.load(file)
    # Check if the name exists in the JSON data
    if value not in data:
        data[value] = ""
        # Save the updated JSON data to the file
        with open(json_file, 'w', encoding='utf8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def create_rdf_political_tenure_and_potical_functions():
    g_political = rdflib.Graph()
    g_political.bind("greek_lp", greek_lp)
    g_political.bind("rdfs", rdfs)
    file_speakers_from_xmls = open(
        './all_speakers_names.json', 'r', encoding='utf8')
    speakers_from_xmls = json.load(file_speakers_from_xmls)
    upourgoi_with_wikidata_file = open(
        './json_files/upourgoi_with_wikidata.json', 'r', encoding='utf8')
    data_upourgoi_with_wikidata_file = json.load(upourgoi_with_wikidata_file)

    parties_with_wikidata_file = open(
        './json_files/parties_with_wikitada.json', 'r', encoding='utf8')
    data_parties = json.load(parties_with_wikidata_file)

    for key, value in data_parties.items():
        g_political.add(
            (URIRef(greek_lp[key]), owl.sameAs, URIRef(value))
        )

    with open('./useful_csv_for_parl_members/_parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv', 'r', encoding='utf8') as file_csv:
        csv_data = (csv.reader(file_csv))
        next(csv_data, None)

        for index, row in enumerate(csv_data):
            subject = URIRef(
                greek_lp[f"political_tenure_{index}"])
            name_speaker = row[6]
            xsd_date_start = datetime.datetime.strptime(
                row[1], "%Y-%m-%d").strftime("%Y-%m-%d")
            xsd_date_end = datetime.datetime.strptime(
                row[2], "%Y-%m-%d").strftime("%Y-%m-%d")
            party = convert_greek_to_english(row[3])
            admin_region = convert_greek_to_english(row[4])
            if name_speaker in speakers_from_xmls:
                id_speaker = speakers_from_xmls[name_speaker]
                subject_for_speaker = URIRef(
                    greek_lp[f"GRmember_{id_speaker}"])
                g_political.add(
                    (subject_for_speaker, greek_lp.PoliticalTenure, subject))
            g_political.add(
                (subject, greek_lp.beginning, Literal(xsd_date_start, datatype=xsd.date)))
            g_political.add(
                (subject, greek_lp.end, Literal(xsd_date_end, datatype=xsd.date)))
            g_political.add(
                (subject, greek_lp.Party, URIRef(greek_lp[party])))
            g_political.add(
                (subject, greek_lp.administrative_region, Literal(admin_region)))
            g_political.add(
                (subject, rdfs.label, Literal(f"Political Tenure {index}", lang="en")))

    roles = set()
    with open('./useful_csv_for_parl_members/_formatted_roles_gov_members_data_11_2023.csv', 'r', encoding='utf8') as file_csv:
        csv_data = (csv.reader(file_csv))
        next(csv_data, None)

        for row in csv_data:
            if len(row) > 1:
                value = row[1]
                if value not in roles:
                    roles.add(value)
                    value_en = convert_greek_to_english(value)
                    g_political.add(
                        (URIRef(f"{greek_lp}role/{value_en}"), rdfs.label, Literal(value, lang="el")))
        file_csv.seek(0)  # Reset the file pointer to the beginning
        next(csv_data, None)
        for index, row in enumerate(csv_data):
            subject = URIRef(
                greek_lp[f"political_function_{index}"])
            name_speaker = row[5]
            xsd_date_start = datetime.datetime.strptime(
                row[2], "%d/%m/%Y").strftime("%Y-%m-%d")
            xsd_date_end = datetime.datetime.strptime(
                row[3], "%d/%m/%Y").strftime("%Y-%m-%d")
            role = row[1]
            if name_speaker in speakers_from_xmls:
                id_speaker = speakers_from_xmls[name_speaker]
                subject_for_speaker = URIRef(
                    greek_lp[f"GRmember_{id_speaker}"])
                g_political.add(
                    (subject_for_speaker, greek_lp.PoliticalFunction, subject))
            if role in roles:
                g_political.add(
                    (subject, greek_lp.institution, URIRef(f"{greek_lp}role/{convert_greek_to_english(role)}")))
            if role in data_upourgoi_with_wikidata_file and data_upourgoi_with_wikidata_file[role]["wiki_link"] != "":
                g_political.add(
                    (subject, schema.about, URIRef(
                        data_upourgoi_with_wikidata_file[role]["wiki_link"]))
                )
            g_political.add(
                (subject, greek_lp.beginning, Literal(xsd_date_start, datatype=xsd.date)))
            g_political.add(
                (subject, greek_lp.end, Literal(xsd_date_end, datatype=xsd.date)))
            g_political.add(
                (subject, rdfs.label, Literal(row[1], lang="el")))

    with open(f"./rdfs/rdf_politicalFunction.rdf", "w", encoding='utf8') as f:
        f.write(g_political.serialize(format='xml'))
    file_speakers_from_xmls.close()
    file_csv.close()
    upourgoi_with_wikidata_file.close()
    parties_with_wikidata_file.close()
    f.close()


# # ! this only one time
# input_file_1 = "./files_from_opa_dritsa/parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv"
# output_file_1 = "./useful_csv_for_parl_members/_parl_members_activity_1989onwards_11_2023_with_gender_merged_file.csv"
# input_file_2 = "./files_from_opa_dritsa/extra_roles_manually_collected.csv"
# output_file_2 = "./useful_csv_for_parl_members/_extra_roles_manually_collected.csv"
# input_file_3 = "./files_from_opa_dritsa/formatted_roles_gov_members_data_11_2023.csv"
# output_file_3 = "./useful_csv_for_parl_members/_formatted_roles_gov_members_data_11_2023.csv"

# # ! this only one time
# add_column_to_csv(input_file_1, output_file_1, 2)
# print("1a-OK")
# add_column_to_csv(input_file_2, output_file_2, 2)
# print("1b-OK")
# add_column_to_csv(input_file_3, output_file_3, 1)
# print("1c-OK")
create_json_official_parl_mem()
print("1d-OK")

print("1-OK")
create_rdf_members_with_details()
print("2-OK")
create_rdf_political_tenure_and_potical_functions()
print("3-OK")
