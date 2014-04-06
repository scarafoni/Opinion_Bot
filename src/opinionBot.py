# opinionBot.py
# Computes ngram data for a given sentence/speech (main method)
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from getLimbaughSpeeches import *
from toMongo import *
import os

# gets all Rush Limbaugh transcripts
# from http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python
def get_limbaugh():
    files = []
    for file in os.listdir("../personalities/limbaugh"):
        if file.endswith(".txt"):
            files.append(file)
    return files


def get_speeches():
    get_limbaugh_speeches('../personalities/limbaugh/',10)

def write_to_mongo():
    l = get_limbaugh()
    for file in l:
        f = open('../personalities/limbaugh/'+file, 'r').read().split('\n')
        if f[1] != '':
            toMongo(f[0], ''.join(f[1:]))

if __name__ == '__main__':
    write_to_mongo()


