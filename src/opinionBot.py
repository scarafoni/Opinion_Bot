# opinionBot.py
# Computes ngram data for a given sentence/speech (main method)
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from getLimbaughSpeeches import *
from toMongo import *
from generateText import *


def get_speeches():
    get_limbaugh_speeches('../personalities/limbaugh/',10)

def write_to_mongo():
    mongo_write()

def generate_probabilities():
    get_probabilities("Rush Limbaugh")

if __name__ == '__main__':
    get_speeches()


