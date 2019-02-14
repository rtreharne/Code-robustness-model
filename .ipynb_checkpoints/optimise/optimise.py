import pandas as pd

def get_ordered_gc(fname):

    #TODO: Read in code from excel block table to data frame

    df = pd.read_excel(fname, header=None)

    #TODO: convert to ORDERED dict

    return df

class CodeOptimise:

    def __init__(self, GC):
        self.GC = GC

if __name__ == "__main__":
    gc = get_ordered_gc("../blastocrithidia_code.xlsx")
    print(gc)

