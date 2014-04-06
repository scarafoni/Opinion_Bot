# toMongo.py
# Adds the ngram data we computed to our instance of MongoDB
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

# from http://api.mongodb.org/python/current/tutorial.html
from pymongo import MongoClient
from ourNgrams import *
from collections import Counter
import os

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
def toMongo(author, speech):
    # break a speech into sentences
    sentences = sentenize(speech)
    # compute the ngram counts
    ngram_counts = [get_ngrams(sentence) for sentence in sentences]
    master_counts = [Counter() for n in range(MAX_NGRAM)]
    # combine the counts together
    for i in range(len(sentences)):
        [master_counts[n].update(ngram_counts[i][n]) for n in range(MAX_NGRAM)]
    # push to mongo speeches
    speech_find = speeches.find_one({"text": speech})
    if speech_find is None:
        ngram_counts_mongo_form = [{' '.join(elem): master_counts[n][elem] for elem in list(master_counts[n])} for n in range(MAX_NGRAM)]
        mongo_speech = {"author": author, 
                        "text": speech,
                        "ngram_counts": ngram_counts_mongo_form,
                        }
        speech_id = speeches.insert(mongo_speech)
        # push to mongo authors
        # if the author is already found, update the existing document
        author_find = authors.find_one({"author": author})
        if author_find is None:
            mongo_author = {"author": author,
                            "speeches": [speech_id]
                            # "ngram_counts": ngram_counts_mongo_form
                            }
            author_id = authors.insert(mongo_author)
        else:
            # in order to update the counts, pull all the information down 
            authors.update({"author": author}, {'$push': {"speeches": speech_id}})
    # return the master counts
    return master_counts

# gets all Rush Limbaugh transcripts
# from http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python
def get_limbaugh():
    files = []
    for file in os.listdir("../personalities/limbaugh"):
        if file.endswith(".txt"):
            files.append(file)
    return files

# writes counts/speeches to MongoHQ
def mongo_write():
    counter = 0
    l = get_limbaugh()
    count_master = [Counter() for n in range(MAX_NGRAM)]
    for file in l:
        f = open('../personalities/limbaugh/'+file, 'r').read().split('\n')
        if f[1] != '':
            new_counts = toMongo(f[0], ''.join(f[1:]))
            print "wrote speech " + file
            if counter < 150:
                [count_master[n].update(new_counts[n]) for n in range(MAX_NGRAM)]
                counter += 1
    # write the counts to the author file
    ngram_counts_mongo_form = [{' '.join(elem): count_master[n][elem] for elem in list(count_master[n])} for n in range(MAX_NGRAM)]
    authors.update({"author": "Rush Limbaugh"}, {"ngram_counts": ngram_counts_mongo_form})






