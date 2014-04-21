#!/usr/bin/python
import sys
import nltk
import string


class Listener():
    '''reads in input from a file and builds a markov table as a result'''
    grammality = 0

    def __init__(self, n, text):
        self.grammality = n
        # strip the punctuation and split the string
        text = text.translate(None, string.punctuation)
        text = ' '.join(text.split())
        # split on whitespace
        self.text = text.split()
        self.model = nltk.NgramModel(self.grammality, self.text)

    def make_story(self, size):
        starters = self.model.generate(10)[-2:]
        word_list = self.model.generate(size, starters)
        print(' '.join(word_list))


if __name__ == '__main__':
    story = open('../stories/'+sys.argv[1]+'.txt', 'r').read()
    listener = Listener(int(sys.argv[2]), story)
    listener.make_story(100)