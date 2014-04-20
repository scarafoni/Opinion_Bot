#!/usr/bin/python
import sys
import nltk
import string


class Listener:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0

    def __init__(self, n, text):
        self.n = n
        # strip the punctuation and split the string
        print('text before', text)
        text = text.translate(None, string.punctuation)
        print(text)
