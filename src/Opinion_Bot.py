#!/usr/bin/python
import sys
import argparse
import nltk

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


if __name__ == '__main__':
    args = init_args.parse_args()
    in_file = args.infile
    out_file = args.outfile
    text = None
    if in_file.name.endswith('.txt'):
        text = in_file.read()
        print('text ', text)
        in_file.close()

    # generate ngrams text
    
    gram_size = args.gramsize
    nltk_text = nltk.Text(text)
    new_sentence = nltk_text.generate(100)
    out_file.write(new_sentence)
    out_file.close()
