import pandas as pd
import itertools
from SGC import *

def get_gilis_val(df, column_label, row_label):
    '''
    This function returns a Gilis value
    :param df: dataframe
    :param column_label: amino code (string)
    :param row_label: amino code (string)
    :return: value (int)
    '''
    return df[column_label][row_label]

def compare_codon(a, b):
    '''
    Compare two codons and return True if they only differ by on base
    :param a: codon (string) e.g. 'UUU'
    :param b: codon (string) e.g. 'UUU'
    :return: boolean
    '''
    if len([i for i in range(len(a)) if a[i] != b[i]]) == 1:
        return True
    else:
        return False

def compare_list_elements(df, sgc):
    sum = 0
    count = 0
    for a, b in itertools.combinations(sgc.keys(), 2):
        if ('Ter' not in [sgc[a], sgc[b]]) and (sgc[a] != sgc[b]):
            count += 1
            if compare_codon(a, b):
                gilis_value = get_gilis_val(df, sgc[a], sgc[b])
                sum += gilis_value
                print(count, [a, b], [sgc[a], sgc[b]], gilis_value, sum)
    return sum


if __name__ == "__main__":
    gilis_df = pd.read_excel('gilis.xlsx')
    sum = compare_list_elements(gilis_df, SGC)
    print(sum)

