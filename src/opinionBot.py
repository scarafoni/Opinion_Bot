# opinionBot.py
# Computes ngram data for a given sentence/speech (main method)
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from getLimbaughSpeeches import *
from toProbabilities import *
from generateText import *


def get_speeches():
    get_limbaugh_speeches('../personalities/limbaugh/',10)

def determine_probabilities():
    print probability_read()

def concat():
    concat_files('../personalities/limbaugh/')

def generate_probabilities():
    get_probabilities("Rush Limbaugh")

def generate():
    get_file_data('../personalities/limbaugh/')

if __name__ == '__main__':
    generate()


