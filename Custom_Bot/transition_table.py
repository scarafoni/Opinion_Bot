class Transition_Table:
    '''holds n-gram transitions for a markov chain'''
    table = {}
    grams = []

    def __init__(self, text_list, grams, n):
        self.grams = grams
        self.gen_dic(grams)
        # populate the table
        for i in range(len(text_list)-n):
            prev_gram = tuple(text_list[i:i+n])
            next_gram = tuple(text_list[i+n-1:i+n+n-1])
            # print(prev_gram, next_gram)
            self.table[prev_gram, next_gram] += 1
        print()
        self.normalize_table()

    def gen_dic(self, grams):
        for gram1 in grams:
            for gram2 in grams:
                self.table[gram1, gram2] = 0

    # normalize the table
    def normalize_table(self):
        for gram in self.grams:
            row = self.get_row_list(gram)
            tot = float(sum(row))
            for col_gram in self.grams:
                if tot != 0:
                    self.table[gram, col_gram] /= tot

    def get_row(self, gram):
        vals = [self.table[gram, gram2] for gram2 in self.grams]
        return dict.fromkeys(self.grams, vals)

    def get_row_list(self, gram):
        return [self.table[gram, gram2] for gram2 in self.grams]

    def get_col(self, gram):
        col = {}
        for row in self.table:
            print(row)
            col[row] = self.table[row][gram]
        return col

    def get(self, gram1, gram2):
        return self.table[gram1, gram2]

    # testing pring function, is usually to big to handle
    def print_table(self):
        for gram1 in self.grams:
            for gram2 in self.grams:
                row_count = 0
                row_count += self.table[gram1, gram2]
                print(gram1, gram2, self.table[gram1, gram2])
            print('row count', row_count)
