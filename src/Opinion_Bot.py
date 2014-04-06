#!/usr/bin/python
import sys
import argparse
from nltk.util import ngrams

# args
init_args = argparse.ArgumentParser(
    description='creates an n-gram markov bot with'
    'very reasonable political opinions indeed')

init_args.add_argument('infile',
                       help='the input file to be read,'
                       'must be either .csv (probability table)'
                       'or .txt (plain text)',
                       type=argparse.FileType('r'))
init_args.add_argument('gramsize',
                       help='the size of the grams for the program',
                       type=int)

init_args.add_argument('-o', '--outfile',
                       help='specify the output of the file,'
                       'must be either .txt (plain text) or .csv'
                       '(markov table), if non specified,'
                       'will print plain text to stdio',
                       type=argparse.FileType('r'),
                       default=sys.stdout)


def main():
    args = init_args.parse_args()
    in_file = args.infile
    out_file = args.outfile
    if in_file.endswith('.txt'):
        text = in_file.read()
    text = out_file.read()

    # generate ngrams text
    gram_size = args.gramsize
    gram_list = ngrams(text, gram_size)
    starting_words = gram_list.generate(100)[-2:]
    content = starting_words.generate(100, starting_words)
    out_file.write(content)
