#!/usr/bin/python
import sys
import argparse
from nltk.util import ngrams
from collections import Counter

#args
init_args = argparse.ArgumentParser()
init_args.add_argument('input', help='the input file to be read, must be either .csv (probability table) or .txt (plain text)',
                       type=argparse.FileType('r')) 
init_args.add_argument('gramsize',help='the size of the grams for the program',
                       type=int)
init_args.add_argument('output', help='specify the output of the file, must be either .txt (plain text) or .csv (markov table), if non specified, will print plain text to stdio',
                       type=argparse.FileType('r'),
                       default=sys.stdout)
init_args.parse_args()


# modified from http://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams
gram_size = init_args.gramsize
counts = []
dicts = []

n_grams = ngrams(sentence.split(), n)
counts.append(n_grams)
dicts.append(Counter(n_grams))

print dicts[1]
