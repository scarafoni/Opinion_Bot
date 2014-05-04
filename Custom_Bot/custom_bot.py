#!/usr/bin/python
import sys
import csv
from nltk import ngrams
import string
from numpy import random, log2
from transition_table import Transition_Table


class Custom_Bot:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0
    text_list = []
    grams = []

    def __init__(self, n, text):
        # text corpus as list of words
        text = text.translate(None, string.punctuation)
        text = ' '.join(text.split())
        self.text_list = text.split()
        # gram number
        self.n = n
        # list of grams
        grams = ngrams(self.text_list, n)
        grams = self.rm_dup(grams)
        self.grams = [tuple(gram) for gram in grams]
        # transition table
        self.table = Transition_Table(self.text_list, self.grams, self.n)

    def get_row(self, gram):
        return self.table.get_row(gram)

    def get_col(self, gram):
        return self.table.get_col(gram)

    # generate a story
    def make_story(self, size):
        starters = self.model.generate(10)[-2:]
        word_list = self.model.generate(size, starters)
        print(' '.join(word_list))

    def rm_dup(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if x not in seen and not seen_add(x)]

    # predict the next word from a given gram
    def predict(self, gram):
        # print('gram', gram)
        row = [key for key, val in self.table.get_row(gram).iteritems()]
        row_probs = [val for key, val in self.table.get_row(gram).iteritems()]
        # print('row probs', row_probs)
        index = random.choice(len(row), 1, p=row_probs)[0]
        # print('prediction', row[index][-1])
        return row[index][-1][-1]

    # wrapper for below two
    def test_H_from_err(self, hint, answer):
        err = self.err_from_prediction(hint, answer)
        return self.H_from_err(err)

    # use fano's inequality to get maximum bound for entropy
    def H_from_err(self, err):
        l = float(len(self.grams))
        return 1.0 + err*log2(l-1.0)

    # returns probability of error
    def err_from_prediction(self, hint, answer):
        # TODO: auto compute number of samples needed
        results = [0.0, 0.0]
        trials = 10.0
        for i in range(int(trials)):
            # print('hint, answer', hint, answer)
            guess = self.predict(hint)
            # print('guess', guess)
            x = 1 if guess == answer else 0
            results[x] += 1.0
        # print([y for y in results])
        return results[0]/trials

#
# end custom_bot
#


def run_tests_exhaustive(story, max_gram):
    with open('../results/H_from_err.csv', 'wb') as f:
        result_csv = csv.writer(f)
        result_csv.writerow(['upper bound H from error'])
        # number of test
        tests = []
        for i in range(2, max_gram):
            print(i)
            test = [str(i)]
            bot = Custom_Bot(i, story)
            print('grams', bot.grams)
            for hint in bot.grams:
                for a in bot.table.get_row(hint):
                    a = a[-1]
                    print('1', 'hint', 'answer', hint, a[-1])
                    # populate the list of tests
                    err = bot.test_H_from_err
                    # test += [err(hint, ans) for j in range(n)]
                    test += [err(hint, a[-1])]
                    # print('test', test)
            tests.append(test)
            print('test final', test)
        # convert the tests to rows, print
        rows = zip(*tests)
        for row in rows:
            result_csv.writerow(row)
        f.close()

#
# main
#

if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    # custom_bot = Custom_Bot(int(sys.argv[2]), story)
    # story, grams, hint, answer
    hint = ('I', 'like', 'apples', 'I', 'like', 'apples',
            'I', 'like', 'apples', 'I')
    run_tests_exhaustive(story, 5)
