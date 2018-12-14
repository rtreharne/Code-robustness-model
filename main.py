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
        if ('Ter' not in [sgc[a], sgc[b]]) and (a != b):
            count += 1
            if compare_codon(a, b):
                gilis_value = get_gilis_val(df, sgc[a], sgc[b])
                sum += gilis_value
                print(count, [a, b], [sgc[a], sgc[b]], gilis_value, sum)
    return sum



purines=['A','G']
pyrimidines=['C','U']



def acquireN(sgc):
    N=0
    for a,b in itertools.combinations(sgc.keys(), 2):
        if('Ter' not in [sgc[a],sgc[b]]) and (a != b):
             if a[0:1] == b[0:1]:
                    if a[1:2] == b[1:2]:
                        if a[2:3] != b[2:3]:
                            N += 1
                    elif a[2:3] == b[2:3]:
                        if (a[1:2] in purines) and (b[1:2] in purines):
                            N += 0.5
                        if (a[1:2] in pyrimidines) and (b[1:2] in pyrimidines):
                            N += 0.5
                        else:
                            N += 0.1
             elif a[1:2] == b[1:2]:
                    if a[2:3] == b[2:3]:
                        if (a[0:1] in purines) and (b[0:1] in purines):
                            N += 1
                        if (a[0:1] in pyrimidines) and (b[0:1] in pyrimidines):
                            N += 1
                        else:
                            N += 0.5
    return N
    print(N)                   
    
# is the loop correct? i think so but N seems very large.

acquireN(SGC)
# is this right? it would make N pretty big. or, since its sum p(c|c')= 1 for any c-
#- does it need divided by 64?

#%%
# order to run function
if __name__ == "__main__":
    gilis_df = pd.read_excel('gilis.xlsx')
    sum = compare_list_elements(gilis_df, SGC)
    print('error cost =' + sum)


# sum p(c|c')= N intially make a function that gets sum
# then rerun but * gilis values by p where p is (correct numerator)/N
#N is the sum of p(c|c') numerators ( 1 for a third base chnage 0.5 for 2nd base transition etc)
#therfore need to make a function that runs through codon comparisons 
# then sums the p(c|c') values 
#not nesessacary for function to returh gilis values 
#after executeing the N function 
#then run gilis compariosn mutiplying the gilis values by th nesacary value over N









