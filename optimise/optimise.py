import pandas as pd
from collections import OrderedDict
from itertools import islice, combinations, chain
import copy

def get_ordered_gc(fname):

    # read in all data from blastocrithidia spreadsheet (block format)
    df = pd.read_excel(fname, header=None)

    # split columns into pairs, each a new dataframe with columns "codon" and "amino"
    df_col_pairs = [df.iloc[:, i*2:i*2+2].rename(columns={i*2:"codon", i*2+1:"amino"}) for i in range(0, int(len(df.columns.values)/2))]

    return pd.concat(df_col_pairs).set_index("codon").to_dict(into=OrderedDict)['amino']

class CodeOptimise:

    def __init__(self, GC):
        self.GC = GC
        self.blocks = self.block_code()

        self.pairwise = self.pairwise_swaps()
        print(len(self.pairwise))
        print(self.pairwise[1])

    def block_code(self, block_size=4):
        blocks = [OrderedDict(islice(self.GC.items(), i*block_size, i*block_size+block_size)) for i in range(0, int(len(self.GC)/block_size))]
        return blocks

    def pairwise_swaps(self):

        pairs = list(combinations(range(len(self.blocks)),2))
        pairwise_swaps = []

        for pair in pairs:
            # does either of the pairs contain stp codon? If so ignore swap.
            merged = list(chain(self.blocks[pair[0]].values(), self.blocks[pair[1]].values()))
            if any('Stp' in string for string in merged):
                print('ignore swap({0}, {1})'.format(pair[0], pair[1]), merged)
            else:
                pairwise_swaps.append(self.swap(pair[0], pair[1]))

        return pairwise_swaps

    def swap(self, index_1, index_2):
        od_1_vals = list(self.blocks[index_1].values())
        od_2_vals = list(self.blocks[index_2].values())

        new_blocks = copy.deepcopy(self.blocks)

        for i, codon in enumerate(self.blocks[index_1]):
            new_blocks[index_1][codon] = od_2_vals[i]
        for i, codon in enumerate(self.blocks[index_2]):
            new_blocks[index_2][codon] = od_1_vals[i]

        return new_blocks


if __name__ == "__main__":
    gc = get_ordered_gc("../blastocrithidia_code.xlsx")
    opt = CodeOptimise(gc)


