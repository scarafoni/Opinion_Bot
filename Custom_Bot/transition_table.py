class Transition_Table:
    '''holds n-gram transitions for a markov chain'''
    table = {}
    grams = []

    def __init__(self, text_list, grams, n):
        self.grams = grams
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
        print('done entering grams')
        self.normalize_table()

    # normalize the table
    def normalize_table(self):
        print('normalizing')
        for gram in self.grams:
            row = self.get_row(gram)
            tot = float(sum(row[col] for col in row))
            for key, val in row.iteritems():
                if tot != 0:
                    self.table[key] /= tot
            # print('finished normalizing row')
            # print(self.get_row(gram))
        print('done normalizing')

    # returns KEYS for prev/next gram combos in a rowj
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
        for gram1 in self.table:
            row_count = 0.0
            for gram2 in self.table[gram1]:
                row_count += self.table[gram1, gram2]
                print(gram1, gram2, self.table[gram1, gram2])
            print('row count', row_count)
