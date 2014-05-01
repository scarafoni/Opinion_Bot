#!/usr/bin/python
import sys
from nltk import ngrams
import string


class Listener:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0
    text_list = []
    grams = []

    def __init__(self, n, text):
        # text corpus as list of words
        text = text.translate(None, string.punctuation)
        text = ' '.join(text.split())
        self.text_list = text.split()
        # gram number
        self.n = n
        # list of grams
        grams = ngrams(self.text_list, n)
        self.grams = [tuple(gram) for gram in grams]
        # transition table
        self.table = Transition_Table(self.text_list, self.grams, self.n)

    # generate a story
    def make_story(self, size):
        starters = self.model.generate(10)[-2:]
        word_list = self.model.generate(size, starters)
        print(' '.join(word_list))


class Transition_Table:
    '''holds n-gram transitions for a markov chain'''

    def __init__(self, text_list, grams, n):
        self.table = dict.fromkeys(grams, dict.fromkeys(grams, 0))
        for i in range(len(text_list) - n + 1 - n):
            prev_gram = tuple(text_list[i:i+n])
            next_gram = tuple(text_list[i+n:i+n+n])
            self.table[prev_gram][next_gram] += 1
        # self.print_table()

    # testing pring function, is usually to big to handle
    def print_table(self):
        for gram1 in self.table:
            for gram2 in gram1:
                print(gram1, gram2, self.table[gram1][gram2])

if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    listener = Listener(int(sys.argv[2]), story)
