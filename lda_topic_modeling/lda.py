
import traceback
import sqlite3
import gensim.corpora as corpora

from nltk.corpus import stopwords
import gensim
from gensim.utils import simple_preprocess
import os
import re
import xml.etree.ElementTree as ET
import multiprocessing


import pyLDAvis.gensim
import pickle
import pyLDAvis
from wordcloud import WordCloud


import nltk
nltk.download('stopwords')

conn = sqlite3.connect(
    'C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/myharvester.db')
cursor = conn.cursor()


stop_words_local_path = "./stopwords/stopwords-el.txt"
my_stop_words_local_path = "./stopwords/my_stopwords.txt"
# Read custom stopwords from a local file
with open(stop_words_local_path, 'r', encoding='utf-8') as file:
    custom_stop_words = file.read().splitlines()
with open(my_stop_words_local_path, 'r', encoding='utf-8') as file:
    my_custom_stop_words = file.read().splitlines()

stop_words = stopwords.words('greek')
stop_words.extend(custom_stop_words)
stop_words.extend(my_custom_stop_words)


def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    filtered_texts = []
    for doc in texts:
        filtered_text = [word for word in simple_preprocess(
            str(doc)) if word not in stop_words]
        filtered_texts.append(filtered_text)
    return filtered_texts


def lda_function(filenames, title):
    akn_namespace = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}

    for index, filename in enumerate(filenames):
        long_string = list()

        tree = ET.parse(filename)
        # Get the root element of the XML tree
        root = tree.getroot()
        # Find the debate section element with name="main_debate_section"
        debate_section = root.find(
            './/akn:debateSection[@name="main_debate_section"]', akn_namespace)
        root.tag = root.tag.replace('{%xsd;}', '%xsd;')
        if debate_section is not None:
            # Extract information from the parsed XML
            speech_elems = root.findall('.//akn:speech', akn_namespace)
            for speech_elem in speech_elems:
                spoken_text_elems = speech_elem.findall(
                    './/akn:p', akn_namespace)
                spoken_text = '\n'.join(
                    [elem.text for elem in spoken_text_elems if elem.text is not None])
                # long_string  += spoken_text
                spoken_text = re.sub('[,\.!?]', '', spoken_text)
                spoken_text = spoken_text.lower()
                long_string.append(spoken_text)

    data_words = list(sent_to_words(long_string))

    # remove stop words
    data_words_ = remove_stopwords(data_words)

    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=100,
                          contour_width=3, contour_color='steelblue')

    # Generate a word cloud
    wordcloud.generate(str(data_words_))

    # Visualize the word cloud
    wordcloud.to_image()
    wordcloud.to_file(f"./wordcloud_img/{title}.png")
    lda_f(data_words_, title)


def lda_f(data_words, title):
    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    num_topics = 30

    # Build LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)

    LDAvis_data_filepath = os.path.join(
        './results/ldavis_prepared_'+str(title))
    # # this is a bit time consuming - make the if statement True
    # # if you want to execute visualization prep yourself
    if 1 == 1:
        LDAvis_prepared = pyLDAvis.gensim.prepare(
            lda_model, corpus, id2word, mds="mmds")
        with open(LDAvis_data_filepath, 'wb') as f:
            pickle.dump(LDAvis_prepared, f)
    # load the pre-prepared pyLDAvis data from disk
    with open(LDAvis_data_filepath, 'rb') as f:
        LDAvis_prepared = pickle.load(f)
    pyLDAvis.save_html(
        LDAvis_prepared, './results/ldavis_prepared_' + str(title) + '.html')
    LDAvis_prepared
    print(f"okkkk {title}\n")


def topic_modelling_per_year():
    try:
        for year in range(1989, 2023):
            filenames = list()
            cursor.execute(
                f"SELECT fileLocalPath, fileLocalName, debateDate FROM debates WHERE strftime('%Y', datetime(debateDate/1000, 'unixepoch')) = '{year}' AND fileLocalName IS NOT NULL")
            rows = cursor.fetchall()
            for row in rows:
                file_path = str("../xml_akn_files/") + \
                    str(row[1]) + str(".xml")
                file_path = file_path.replace("//", "/")
                if os.path.exists(file_path):
                    filenames.append(file_path)
            if (len(filenames) > 0):
                print(year, len(filenames))
                title = f"{year}"
                lda_function(filenames, title)

    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())


def starting_funtion():
    topic_modelling_per_year()


if __name__ == '__main__':
    # Add this line to support multiprocessing on Windows
    multiprocessing.freeze_support()
    starting_funtion()
