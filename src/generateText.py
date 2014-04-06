# generateText.py
# Given n-gram probabilities, generates new text
# in the style of a politician/pundit
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from pymongo import MongoClient
from ourNgrams import *

# sets up connection to MongoHQ
f = open('mongospecs.txt')
[user, password] = f.read().split()
client = MongoClient('mongodb://' + str(user) + ':' + str(password) + '@oceanic.mongohq.com:10096/opinion_bot')
db = client['opinion_bot']
speeches = db['speeches']
authors = db['authors']

# retrieves the n-gram counts from MongoHQ
def get_counts_data(author):
    auth = authors.find_one({"author": author})
    return auth['ngram_counts']

# gets the n-gram probabilities for a given author
def get_probabilities(author):
    ngram_data = get_counts_data(author)
    # enumerates unigram, bigram, ..., ngram probabilities

    for n in range(MAX_NGRAM):
        pass
        # LEFT OFF HERE



