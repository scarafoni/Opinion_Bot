#!/usr/bin/python
import sys
import csv
from nltk import ngrams
import string
from numpy import random, log2, mean
from transition_table import Transition_Table


class Opinion_Bot:
    '''reads in input from a file and builds a markov table as a result'''
    n = 0
    text_list = []
    grams = {}

    def __init__(self, n, text):
        text = text.translate(None, string.punctuation)
        text = ' '.join(text.split())
        self.text_list = text.split()
        self.n = n

        # list of grams
        grams = ngrams(self.text_list, n)
        grams_nd = self.rm_dup(grams)
        self.grams = {tuple(gram): float(grams.count(gram)) for gram in grams_nd}

        # transition table
        self.table = Transition_Table(self.text_list, self.grams,
                                      self.n, len(grams))

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
        row = [key for key, val in self.table.get_row(gram).iteritems()]
        row_probs = [val for key, val in self.table.get_row(gram).iteritems()]
        index = random.choice(len(row), 1, p=row_probs)[0]
        return row[index][-1][-1]

    # wrapper for below two
    def test_H_from_err(self, hint, answer):
        row = [key for key, val in self.table.get_row(hint).iteritems()]
        l = float(len(row))
        err = 1 - self.table.get(hint, answer)
        return self.H_from_err(err, l)

    # use fano's inequality to get maximum bound for entropy
    def H_from_err(self, err, l):
        he = (-1.0*log2(err)) - ((1.0-err)*log2(1.0-err)) if err > 0 else -((1.0-err)*log2(1.0-err))
        return he + (err*log2(l)-1) if err > 0.0 else 0.0

    # returns probability of error
    def err_from_prediction(self, hint, answer, l):
        if l == 1:
            # print('only one option on',hint)
            return 0
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

    def H_from_table(self):
        tot = 0.0
        for gram in self.table.grams:
            row = self.table.get_row(gram)
            mu = self.table.gram_probs[gram]
            for key, val in row.iteritems():
                # print('key, val', key, val)
                tot += (mu * val * log2(val))
        return -1.0 * tot
#
# end custom_bot
#


def test_H_from_table(story, save_file, min_gram, max_gram):
    with open('../results/'+save_file, 'wb') as f:
        result_csv = csv.writer(f)
        result_csv.writerow(['H from table'])
        for i in range(min_gram, max_gram+1):
            bot = Opinion_Bot(i, story)
            x = bot.H_from_table()
            print(x)
            result_csv.writerow([str(x)])
        f.close()

''' calculate H from teh totality of the MC table '''
def run_tests_exhaustive(story, save_file, min_gram, max_gram):
    with open('../results/'+save_file, 'wb') as f:
        result_csv = csv.writer(f)
        result_csv.writerow(['upper bound H from error'])
        # number of test
        tests = []
        for i in range(min_gram, max_gram+1):
            # print(i)
            test = [str(i)]
            bot = Opinion_Bot(i, story)
            # print('grams', bot.grams)
            i = 0
            tsize = len(bot.grams)
            for hint in bot.grams:
                if not i % 10:
                    print('on gram '+str(i)+' of '+str(tsize))
                for a in bot.table.get_row(hint):
                    a = a[-1]
                    err = bot.test_H_from_err
                    test += [err(hint, a)]
                i += 1
            tests.append(test)
            print('test final', test)
        # convert the tests to rows, print
        for row in tests:
            result_csv.writerow(row)
        f.close()

''' calculate H just from a sample size '''
def run_tests_mc(story, save_file, min_gram, max_gram, num_tests):
    with open('results/'+save_file, 'wb') as f:
        result_csv = csv.writer(f)
        result_csv.writerow(['upper bound H from error'])
        # number of test
        tests = []
        for i in range(min_gram, max_gram+1):
            print('on gram '+str(i)+' of '+str(max_gram))
            test = [str(i)]
            bot = Opinion_Bot(i, story)
            # print('grams', bot.grams)
            gram_keys = bot.grams.keys()
            num_grams = len(gram_keys)
            for j in range(num_tests):
                hint = random.randint(num_grams)
                hint = gram_keys[hint]
                row = bot.table.get_row(hint)
                while len(row) == 0:
                    hint = random.randint(num_grams)
                    hint = gram_keys[hint]
                    row = bot.table.get_row(hint)
                ax = random.randint(len(row))
                a = row.keys()[ax]
                a = a[-1]
                err = bot.test_H_from_err
                test += [err(hint, a)]
            tests.append(test)
            print('average',mean([float(x) for x in test[1:]]))
        for row in tests:
            result_csv.writerow(row)
        f.close()
#
# main
#

if __name__ == '__main__':
    story = open('texts/'+sys.argv[1], 'r').read()
    save_file = sys.argv[2]
    min_gram = int(sys.argv[3])
    max_gram = int(sys.argv[4])
    # story, grams, hint, answer
    # test_H_from_table(story, save_file, min_gram, max_gram)
    # run_tests_exhaustive(story, save_file, min_gram, max_gram)
    run_tests_mc(story, save_file, min_gram, max_gram)
