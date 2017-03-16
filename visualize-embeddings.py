# -*- coding: utf-8 -*-

import os
import csv
from rosette.api import API, DocumentParameters
import codecs
class Document(object):
    def __init__(self, filepath, category, headline, content):
        self.filepath = filepath
        self.category = category
        self.headline = headline
        self.content = content

def parse_bbc_data():
    """
    Read data from the bbc 5-categories corpus into Document objects
    see: http://mlg.ucd.ie/datasets/bbc.html
    """
    categories = [u"business", u"entertainment", u"politics", u"sport", u"tech"]
    for category in categories:
        category_dir_path = os.path.join("bbc", category)
        for filename in os.listdir(category_dir_path):
            filepath = os.path.join(category_dir_path, filename)
            with codecs.open(filepath, "r", "latin1") as ifh:
                headline = ifh.readline()
                content = ifh.read()
                yield Document(filepath, category, headline.strip(), content.strip())

def vectorize_text(text, key=os.environ['MY_ROSAPI_KEY'], url='https://api.rosette.com/rest/v1/'):
    """
    Return the vector representation of the input text (as a list of floats).
    """
    api = API(user_key=key, service_url=url)
    params = DocumentParameters()
    params["content"] = text
    return api.text_embedding(params)["embedding"]

if __name__ == '__main__':
    METADATA_FILE_NAME = "metadata.tsv"
    EMBEDDINGS_FILE_NAME = "embeddings.tsv"
    docs = list(parse_bbc_data())

    # Iterate over the Documents and create the output files
    with open(EMBEDDINGS_FILE_NAME, "wb") as embeddings_fh:
        with open(METADATA_FILE_NAME, "wb") as metadata_fh:
            embeddings_writer = csv.writer(embeddings_fh, delimiter='\t', lineterminator="\n")
            metadata_writer = csv.writer(metadata_fh, delimiter='\t', lineterminator="\n")
            metadata_writer.writerow(["Category", "Headline"])
            for doc in docs:
                print len(vectorize_text(doc.content))
                embeddings_writer.writerow(vectorize_text(doc.content))
                metadata_writer.writerow([doc.category, doc.headline.encode('utf-8')])


    print ("The {} and {} files have been created successfully.".format(EMBEDDINGS_FILE_NAME, METADATA_FILE_NAME))
