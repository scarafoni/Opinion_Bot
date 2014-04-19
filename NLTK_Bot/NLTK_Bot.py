#!/usr/bin/python
import sys
import nltk

class Listener:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0
    nltk.ngram model
    
    def __init__(self,n,text):
        self.n = n
        #strip the punctuation and split the string
        print('text before',text)
        text = text.translate(None,string.punctuation)
        print(text)



if __name__ == '__main__':
    model = Listener(2,"this sentence has a . misplaced period,")

