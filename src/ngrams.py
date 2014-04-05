

# modified from http://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams

from nltk.util import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print grams