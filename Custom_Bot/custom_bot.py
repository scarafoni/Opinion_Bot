#!/usr/bin/python
import sys
from nltk import ngrams
import string
from transition_table import Transition_Table


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

    def get_row(self, gram):
        return self.table.get_row(gram)

    def get_col(self, gram):
        return self.table.get_col(gram)

    # generate a story
    def make_story(self, size):
        starters = self.model.generate(10)[-2:]
        word_list = self.model.generate(size, starters)
        print(' '.join(word_list))
    '''
    def conditional_entropy(dist):
        sum = 0
        for val in dist:
           sum += dist[val]* 
    '''


if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    listener = Listener(int(sys.argv[2]), story)
    print(listener.get_row(("to", "the")))
