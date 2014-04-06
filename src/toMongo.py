# toMongo.py
# Adds the ngram data we computed to our instance of MongoDB
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

# from http://api.mongodb.org/python/current/tutorial.html
from pymongo import MongoClient
from ourNgrams import *
from collections import Counter

# sets up connection to MongoHQ
f = open('mongospecs.txt')
[user, password] = f.read().split()
client = MongoClient('mongodb://' + str(user) + ':' + str(password) + '@oceanic.mongohq.com:10096/opinion_bot')
db = client['opinion_bot']
speeches = db['speeches']
authors = db['authors']

# inputs a speech (tuple of author, transcription)
# does some intermediary work (like calculating ngrams from ngrams.py)
# outputs True if successfully exported data to MongoHQ instance and False otherwise
def toMongo(speech):
    # break a speech into sentences
    sentences = sentenize(speech)
    # compute the ngram counts
    ngram_counts = [get_ngrams(sentence) for sentence in sentences]
    master_counts = [Counter() for n in range(MAX_NGRAM)]
    # combine the counts together
    for i in range(len(sentences)):
        [master_counts[n].update(ngram_counts[i][n]) for n in range(MAX_NGRAM)]
    return master_counts

