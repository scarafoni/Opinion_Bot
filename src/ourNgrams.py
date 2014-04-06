# ngrams.py
# Computes ngram data for a given sentence/speech
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014


# modified from http://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams
from nltk.util import ngrams
from collections import Counter
import string

MAX_NGRAM = 6


# Computes n-gram counts for words in a given sentence
def get_ngrams(sentence):
    dicts = []
    # go through each 1-gram, 2-gram, ..., n-gram
    for n in range(MAX_NGRAM):
        # compute ngrams
        n_grams = ngrams(tokenize(sentence), n+1)
        dicts.append(Counter(n_grams))
    return dicts

# splits the sentence into specific words, and gets rid of punctuation, extra
# whitespace, and other crap
def tokenize(sentence):
    # from http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    punc = sentence.translate(None, string.punctuation)
    lower = punc.lower()
    return lower.split()

# splits the speech into sentences (text separated by a '.')
def sentenize(speech):
    # NOTE: this is not fool-proof, there might be periods in the middle of a sentence.
    # Nevertheless, it is a good start and we can change it later if need be.
    # It should be a good heuristic though.
    return speech.split('.')



