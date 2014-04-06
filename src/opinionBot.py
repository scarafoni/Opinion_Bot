# opinionBot.py
# Computes ngram data for a given sentence/speech (main method)
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from getLimbaughSpeeches import *
from toMongo import *


def get_speeches():
    get_limbaugh_speeches('../personalities/limbaugh/',100)

def write_to_mongo():
    mongo_write()

if __name__ == '__main__':
    write_to_mongo()


