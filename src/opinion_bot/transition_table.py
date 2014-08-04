import itertools
class Transition_Table:
    '''holds n-gram transitions for a markov chain'''
    table = {}
    grams = []
    gram_probs = {}
    text_size = 0.0

    def __init__(self, text_list, grams, n, text_size):
        self.grams = grams.keys()
        self.gram_probs = grams
        self.text_size = float(text_size)
        # self.gen_dic(grams)
        # self.table = dict.fromkeys(grams, {})
        # populate the table
        for i in range(len(text_list)-n):
            prev_gram = tuple(text_list[i:i+n])
            next_gram = tuple(text_list[i+1:i+n+1])
            # print(prev_gram, next_gram)
            if (prev_gram, next_gram) in self.table:
                self.table[prev_gram, next_gram] += 1
            else:
                self.table[prev_gram, next_gram] = 1
        self.normalize_table()

    ''' normalize the table (all rows probabilities add to 1 '''
    def normalize_table(self):
        for gram in self.grams:
            row = self.get_row(gram)
            tot = float(sum(row[col] for col in row))
            # calculate the total instances of this gram
            for key, val in row.iteritems():
                if tot != 0:
                    self.table[key] /= tot

    ''' returns KEYS for prev/next gram combos in a row '''
    def get_row(self, gram):
        row = {}
        for key, value in self.table.iteritems():
            if key[0] == gram:
                row[key] = value
        return row

    def get_col(self, gram):
        vals = [self.table[gram2, gram] for gram2 in self.grams]
        return dict.fromkeys(self.grams, vals)

    def get_col_list(self, gram):
        return [self.table[gram2, gram] for gram2 in self.grams]

    def get(self, gram1, gram2):
        return self.table[gram1, gram2]

    # testing pring function, is usually to big to handle
    def print_table(self):
        for gram1, gram2 in itertools.product(*[self.table, self.table[gram1]]):
            print(gram1, gram2, self.table[gram1, gram2])
        '''
        for gram1 in self.table:
            row_count = 0.0
            for gram2 in self.table[gram1]:
                row_count += self.table[gram1, gram2]
                print(gram1, gram2, self.table[gram1, gram2])
        '''
