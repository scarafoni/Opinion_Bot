import unittest
import csv
from numpy import random, mean
from opinion_bot.opinion_bot import Opinion_Bot

class Test_Opinion_Bot(unittest.TestCase):
    
    def run_tests_mc(self,story, save_file, min_gram, max_gram):
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
                for j in range(100):
                    hint = random.randint(num_grams)
                    hint = gram_keys[hint]
                    row = bot.table.get_row(hint)
                    while len(row) == 0:
                        hint = random.randint(num_grams)
                        hint = gram_keys[hint]
                        row = bot.table.get_row(hint)
                    ax = random.randint(len(row))
                    # print('ax',ax)
                    # print('hint',hint)
                    # print('key',row.keys())
                    a = row.keys()[ax]
                    # print('a',a)
                    a = a[-1]
                    # print('1', 'hint', 'answer', hint, a[-1])
                    # populate the list of tests
                    err = bot.test_H_from_err
                    # test += [err(hint, ans) for j in range(n)]
                    test += [err(hint, a)]
                    # print('test', test)
                tests.append(test)
                # print('test final', test)
                print('average',mean([float(x) for x in test[1:]]))
            for row in tests:
                result_csv.writerow(row)
            f.close()