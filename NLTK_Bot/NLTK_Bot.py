#!/usr/bin/python
# import sys
import nltk
import string


class Listener:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0

    def __init__(self, n, text):
        self.n = n
        # strip the punctuation and split the string
        text = text.translate(None, string.punctuation)
        text = ' '.join(text.split())
        self.text = text.split()
        print(self.text)
        self.model = nltk.NgramModel(n=self.n, train=self.text)
        print(self.model.generate(10))

    def make_story(size):
        word_list = self.model.generate(size)
        print(' '.join(word_list))


if __name__ == '__main__':
    story = open('../stories/random1.txt','r').read()
    listener = Listener(2, story)
