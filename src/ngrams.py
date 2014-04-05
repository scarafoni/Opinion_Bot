

# modified from http://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams

from nltk.util import ngrams
from collections import Counter
sentence = 'this is a foo bar foo bar i want to ngramize it'

MAX_NGRAM = 6
counts = []
dicts = []

for n in range(1,MAX_NGRAM+1):
    n_grams = ngrams(sentence.split(), n)
    counts.append(n_grams)
    dicts.append(Counter(n_grams))

print dicts[1]