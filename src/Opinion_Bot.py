#!/usr/bin/python
import sys
import argparse
import nltk
import warnings
warnings.simplefilter('ignore')

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
                       type=argparse.FileType('a'),
                       default=sys.stdout)


if __name__ == '__main__':
    args = init_args.parse_args()
    gram_size = args.gramsize
    in_file = args.infile
    out_file = args.outfile
    text = None
    if in_file.name.endswith('.txt'):
        tokens = nltk.word_tokenize(in_file.read())
        text = nltk.Text(tokens)
        in_file.close()

    # generate ngrams text
    model = nltk.NgramModel(gram_size, text)
    starting_words = model.generate(100)[-2:]
    model_words = model.generate(50, starting_words)
    speech = ' '.join([word for word in model_words])
    print(speech)
    out_file.write(speech)
    out_file.close()
