#!/usr/bin/python
import sys
from nltk import ngrams
import string
from numpy import random
from transition_table import Transition_Table


class Custom_Bot:
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
        grams = self.rm_dup(grams)
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

    def rm_dup(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if x not in seen and not seen_add(x)]

    # predict the next word from a given gram
    def predict(self, gram):
        row = self.table.get_row_list(gram)
        index = random.choice(len(self.grams), 1, p=row)[0]
        return self.grams[index][self.n-1]
       
    def H_from_Err(self,err)
    '''
    def conditional_entropy(gram):
        sum = 0
        for val in gram: 
           sum += dist[val]
    '''

if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    listener = Custom_Bot(int(sys.argv[2]), story)
    for i in range(100):
        print(listener.predict(('like', 'apples')))
