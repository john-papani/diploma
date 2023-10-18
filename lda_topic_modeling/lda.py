
from collections import defaultdict
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
# nltk.download('stopwords')
import spacy

# conn = sqlite3.connect(
#      '/home/ipap/john_files/myharvester_serverPaths.db')
# cursor = conn.cursor()

conn = sqlite3.connect(
   "C:/Users/johnp/Documents/ECE_NTUA/diploma/official_data_fromKoniaris/myharvester.db")
cursor = conn.cursor()


stop_words_local_path = "./stopwords/stopwords-el.txt"
my_stop_words_local_path = "./stopwords/my_stopwords.txt"
stop_words_spacy_local_path = "./stopwords/stopwords_el_spacy.txt"
# Read custom stopwords from a local file
with open(stop_words_local_path, 'r', encoding='utf-8') as file:
    custom_stop_words = file.read().splitlines()
with open(my_stop_words_local_path, 'r', encoding='utf-8') as file:
    my_custom_stop_words = file.read().splitlines()
with open(stop_words_spacy_local_path, 'r', encoding='utf-8') as file:
    stop_words_spacy = file.read().splitlines()

stop_words = stopwords.words('greek')
stop_words.extend(stopwords.words('english'))
stop_words.extend(custom_stop_words)
stop_words.extend(my_custom_stop_words)
stop_words.extend(stop_words_spacy)

stop_words = set(stop_words)

top_terms_sorted_30 = open('./top_terms_sorted_30.txt', 'a', encoding="utf8")
top_terms_sorted_10 = open('./top_terms_sorted_10.txt', 'a', encoding="utf8")

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))

def process_text(sentences):
    nlp = spacy.load("el_core_news_lg")
    processed_texts = []
    total_sum = 0
    for sublist in sentences:
        total_sum += len(sublist)
    nlp.max_length = total_sum + 100
    print(total_sum)
    for sentence in sentences:
        # Tokenize using gensim's simple_preprocess with deacc=True
        filtered_text = simple_preprocess(str(sentence), deacc=True)

        # Remove stopwords
        filtered_text = [
            word for word in filtered_text if word not in stop_words]

        # Join the filtered words into a single string
        cleaned_text = ' '.join(filtered_text)

        # Apply spaCy lemmatization
        doc = nlp(cleaned_text)
        lemmas = [token.lemma_ for token in doc]
        # Remove stopwords from lemmas
        lemmas = [lemma for lemma in lemmas if lemma not in stop_words]

        processed_texts.append(lemmas)

    return processed_texts


def lda_function(filenames, title):
    akn_namespace = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}

    long_string = list()
    for filename in filenames:
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
                spoken_text = re.sub('[,\.!?]', '', spoken_text)
                spoken_text = spoken_text.lower()
                long_string.append(spoken_text)

    print(title, len(long_string))
    lemmatized_texts = process_text(long_string)

    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=100,
                          contour_width=3, contour_color='steelblue')

    # Generate a word cloud
    wordcloud.generate(str(lemmatized_texts))

    # Visualize the word cloud
    wordcloud.to_image()
    wordcloud.to_file(f"./wordcloud_img/{title}.png")

    lda_f(lemmatized_texts, title)


def lda_f(data_words, title):
    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    num_topics = 6

    # Build LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                 id2word=id2word,
                                                 num_topics=num_topics,
                                                 random_state=100,
                                                 passes=30,
                                                 alpha=50/num_topics,
                                                 eta=0.1,
                                                 per_word_topics=True)
    #lda_model = gensim.models.LdaMulticore(corpus=corpus,
    #                                      id2word=id2word,
    #                                     num_topics=num_topics)

    # Calculate overall term frequency for each term in the corpus
    term_freq = defaultdict(int)
    for doc in corpus:
        for word_id, freq in doc:
            term_freq[id2word[word_id]] += freq

    # Print the top 30 most salient terms overall
    overall_top_terms_30 = sorted(
        term_freq.items(), key=lambda x: x[1], reverse=True)[:30]
    top_terms_sorted_30.write(
        f"\n\nYear:{title} -- Top 30 Most Salient Terms Overall:\n")
    for term, freq in overall_top_terms_30:
        top_terms_sorted_30.write(f"{term}: {freq}\n")

    # Print the top 10 most salient terms overall
    overall_top_terms_10 = sorted(
        term_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    top_terms_sorted_10.write(
        f"\n\nYear:{title} -- Top 10 Most Salient Terms Overall:\n")
    for term, freq in overall_top_terms_10:
        top_terms_sorted_10.write(f"{term}: {freq}\n")
       
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
            # if (len(filenames) > 0):
            #     print(year, len(filenames))
            #     title = f"{year}"
            #     datapath = "C:/Users/johnp/Desktop/test/"
            #     files = sorted([f for f in os.listdir(
            #         datapath) if not f.startswith('.')])
            #     print(files)
            #     lda_function(files, "testing")
            # break

    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())


def starting_funtion():
    topic_modelling_per_year()

if __name__ == '__main__':
    # Add this line to support multiprocessing on Windows
    multiprocessing.freeze_support()
    starting_funtion()
