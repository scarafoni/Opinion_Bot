# generateText.py
# Given n-gram probabilities, generates new text
# in the style of a politician/pundit
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from pymongo import MongoClient
from ourNgrams import *
from nltk import *

# # sets up connection to MongoHQ
# f = open('mongospecs.txt')
# [user, password] = f.read().split()
# client = MongoClient('mongodb://' + str(user) + ':' + str(password) + '@oceanic.mongohq.com:10096/opinion_bot')
# db = client['opinion_bot']
# speeches = db['speeches']
# authors = db['authors']

# retrieves the n-gram counts from MongoHQ
def get_counts_data(author):
    auth = authors.find_one({"author": author})
    print auth
    return auth['ngram_counts']

# gets the n-gram probabilities for a given author
def get_probabilities(author):
    # first get the n-gram counts for the author
    ngram_data = get_counts_data(author)
    # then split the string (for 2-grams and above into a tuple)
    ngram_split = [{tup[0].split(): tup[1] for tup in igram} for igram in ngram_split]
    # enumerates unigram, bigram, ..., ngram probabilities
    # first enumerate the totals
    totals = [float(sum(ngram_data[i].values())) for i in range(MAX_NGRAM)]
    totals.insert(0,1.0)
    # then go through 1-gram to n-gram, getting probabilities for each n-gram transition
    unigram_probabilities = {tup[0]: tup[1]/totals[1] for tup in ngram_split[0]}
    print unigram_probabilities


def get_file_data(folder):
    f = open(folder + 'MASTER.txt', 'r').read()
    text = Text(word_tokenize(f))
    new_sentence = generate(text, 100, 4)

# from the NLTK documentation
def generate(text, length=100, gram=3):
        """
        Print random text, generated using a trigram language model.

        :param length: The length of text to generate (default=100)
        :type length: int
        :seealso: NgramModel
        """
        estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
        _trigram_model = NgramModel(gram, text, estimator=estimator)
        text = _trigram_model.generate(length)
        print(tokenwrap(text))





