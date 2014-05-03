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
        row = self.table.get_row_list(gram)
        index = random.choice(len(self.grams), 1, p=row)[0]
        return self.grams[index][self.n-1]

    # wrapper for below two
    def test_H_from_err(self, hint, answer):
        err = self.err_from_prediction(hint, answer)
        return self.H_from_err(err)

    # returns probability of error
    def err_from_prediction(self, hint, answer):
        # TODO: auto compute number of samples needed
        results = [0.0, 0.0]
        trials = 10.0
        for i in range(int(trials)):
            # print(results)
            guess = self.predict(hint)
            # print(guess, answer)
            x = 1 if guess == answer else 0
            results[x] += 1.0
        # print([y/trials for y in results])
        return results[0]/trials

    # use fano's inequality to get maximum bound for entropy
    def H_from_err(self, err):
        l = float(len(self.grams))
        return 1.0 + err*log2(l-1.0)

#
# end custom_bot
#


def run_tests(story, max_gram, hint, answer):
    with open('../results/H_from_err.csv', 'wb') as f:
        result_csv = csv.writer(f)
        result_csv.writerow(['upper bound H from error'])
        # number of test
        n = 5
        tests = []
        for i in range(2, max_gram):
            print('i', i)
            bot = Custom_Bot(i, story)
            test = [str(i)]
            # TODO- figure out amount to test
            test += [bot.test_H_from_err(hint, answer) for j in range(n)]
            tests.append(test)
        # convert the tests to rows, print
        rows = zip(*tests)
        for row in rows:
            result_csv.writerow(row)
        f.close()

if __name__ == '__main__':
    story = open('../texts/'+sys.argv[1], 'r').read()
    # custom_bot = Custom_Bot(int(sys.argv[2]), story)
    # story, grams, hint, answer
    run_tests(story, 4, ('I', 'like'), 'apples')
