# toProbabilities.py
# Computes the ngram data from txt files
# Dan Scarafoni, J. Hassler Thurston
# HackNY Fall 2014 Hackathon
# April 5-6, 2014

from ourNgrams import *
from collections import Counter
import os

# inputs a speech (tuple of author, transcription)
# does some intermediary work (like calculating ngrams from ngrams.py)
# outputs True if successfully exported data to MongoHQ instance and False otherwise
def toMongo(author, speech):
    # break a speech into sentences
    sentences = sentenize(speech)
    # compute the ngram counts
    ngram_counts = [get_ngrams(sentence) for sentence in sentences]
    master_counts = [Counter() for n in range(MAX_NGRAM)]
    # combine the counts together
    for i in range(len(sentences)):
        [master_counts[n].update(ngram_counts[i][n]) for n in range(MAX_NGRAM)]
    return master_counts

# gets all Rush Limbaugh transcripts
# from http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python
def get_limbaugh(folder):
    files = []
    for file in os.listdir(folder):
        if file.endswith(".txt") and not file.endswith("MASTER.txt"):
            files.append(file)
    return files

# writes counts/speeches to MongoHQ
def probability_read():
    l = get_limbaugh()
    count_master = [Counter() for n in range(MAX_NGRAM)]
    for file in l:
        f = open('../personalities/limbaugh/'+file, 'r').read().split('\n')
        if f[1] != '':
            new_counts = toMongo(f[0], ''.join(f[1:]))
            [count_master[n].update(new_counts[n]) for n in range(MAX_NGRAM)]
    return count_master


# concatenates all text files into one (called MASTER.txt)
def concat_files(folder):
    f = open(folder + "MASTER.txt", 'w')
    l = get_limbaugh(folder)
    for file in l:
        f1 = open(folder+file, 'r').read().split('\n')
        if f1[1] != '':
            f.write(' '.join(f1[1:]))

# reads files
def file_read():
    l = get_limbaugh()
    for file in l:
        f = open('../personalities/limbaugh/'+file, 'r').read().split('\n')
        if f[1] != '':
            new_counts = toMongo(f[0], ''.join(f[1:]))
            [count_master[n].update(new_counts[n]) for n in range(MAX_NGRAM)]
    return count_master


