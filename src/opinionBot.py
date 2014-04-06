# opinionBot.py
# Computes ngram data for a given sentence/speech (main method)
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from toMongo import *


def main():
    f = open('../personalities/mac_lover.txt')
    tm = toMongo("Rush Limbaugh", f.read())
    print tm
    f.close()

if __name__ == '__main__':
    main()


