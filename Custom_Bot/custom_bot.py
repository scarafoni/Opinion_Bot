#!/usr/bin/python
import sys
from nltk import ngrams
import string


class Listener():
    '''reads in input from a file and builds a markov table as a result'''
    n = 0

    def __init__(self, n, text):
        # strip the punctuation and split the string
        text = text.translate(None, string.punctuation)
        self.text = ' '.join(text.split())
        # split on whitespace
        self.text_list = text.split()
        # enter the relevant information
        self.n = n
        self.grams = ngrams(self.text_list, n)
        self.table = Transition_Table(self.grams)

    def make_story(self, size):
        starters = self.model.generate(10)[-2:]
        word_list = self.model.generate(size, starters)
        print(' '.join(word_list))


class Transition_Table:
    '''holds n-gram transitions for a markov chain'''

    def __init__(self, grams):
        self.table = dict.fromkeys(grams, dict.fromkeys(grams, 0))

    def populate_table(self, text_list, n):
        for i in range(len(text_list) - n + 1 - n):
            prev_gram = text_list[i:i+n]
            next_gram = text_list[i+n:i+(2*n)]
            self.table[prev_gram][next_gram] += 1

    # testing pring function, is usually to big to handle
    def print_table(self):
        

if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    listener = Listener(int(sys.argv[2]), story)
