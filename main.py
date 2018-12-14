import pandas as import pd

# read 'gilis.xlsx' to dataframe
gilis_df = pd.read_excel('gilis.xlsx')





# may need to change codon and amino acid around to work with .keys
# but not sure if haveing mutiple keys of the same name is allowed, probably not

SGC={"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
    "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
    "UAU":"Tyr", "UAC":"Tyr", "UAA":"Ter", "UAG":"Ter",
    "UGU":"Cys", "UGC":"Cys", "UGA":"Ter", "UGG":"Trp",
    "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
    "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
    "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
    "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
    "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
    "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
    "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
    "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
    "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
    "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
    "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
    "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}

# dictionary within dictionary of what each codn turns in to

print(SGC.keys()) # gives SGC codons as a list
print(SGC.values()) # gives SGC amino acids as a list
# for key in SGC will give codons, use in loop to compare codons?
# dict.items gives key and value pairs, could also be a way to compare

# prints first 2 bases of codons, sliceing keys as string seems the way to go
for key in SGC.keys():
    print(key[0:1]) # slices key and prints first base only

purines=['A','G']
pyrimidines=['C','U']

sumError=()
p=1

# think omething like this but for every single base chnage would work BUT this syntax-
#literally compares a key to its self, need to find way to compare to others
for key1 in SGC.keys():
    for key2 in SGC.keys():
        if SGC.keys(key1) != SGC.keys(key2):
            if SGC[key1] != 'Ter':
                if key1[0:1] == key2[0:1]:
                    if key1[1:2] == key2[1:2]:
                        if not key1[2:3] == key2[2:3]:
                            (gilis) # use purine/pyrimidine to get p later
                            sumError += (p* gilis) # if SGC[key2] == 'Ter (for stop later)
                    elif key1[2:3] == key2[2:3]:
                        (gilis)
                        sumError += (p*gilis)
                elif key1[1:2] == key2[1:2]:
                    if key1[2:3] == key2[2:3]:
                       (gilis) # SGC[key1] SGC[key2]
                       sumError += (p*gilis)

# do gilis spreadsheet
# make github repo
# send rob link

# how to compare base make up of codons? for value in key? (makes a nested loop)
# or make a function that compares codon base makeup so only one line in loop?
# def functions U/A/C/G count(Key): key.count ('U/A/C/G') ?
#insert  functions in loop then compare each of two keys, if differ by no more than one-
#-base then in theory codons only differ by one base, so the key value should be compared-
#-however its unclear how this method could distinguish transistions and transversions
#-also unclear on how to distiguish base change position (p(c|c'))

#if possible could devide the dict key (codon) into a list of the three bases-
#then run through if statements e.g. if key1[0] == key2[0]:-
#can run through this to isolate the postion of mutation in codons differing by one base-
#once this is done compare if the bases in each key at the differing position are-
#-either both purine/pyrimidine or diffferent
#this would distigush tristion and tranversion, as well as the base position
#therefore p(c|c') could be calculated.

purines=['A','G']
pyrimidines=['C','U']

# gives codon and amino acid pair outputs, possible to rename key to codon and value to AA?
for key,value in SGC.items():
    print(key,value)

# for key in SGC, compare codon base make up, then compare the value of the keys-
# -in the loop if only one base difference. if key1.value == key2.value +7?

Gilis=1
# need a way to code Gilis matrix, use a 2D numpy array?
# np.mat is meant to make matrixs, but i'm ulnclear how to make Gilis useing it
# possible that Gilis matirx is not the same as what python/numpy calls a matrix?
# maybe need to write out a square array of Gilis and make an array of it?
# possible to make Gilis array in excel, read th file with open or pandas, and make -
# - an array of the file data?
# assign numerical value to AA combinations for numpy array, or assign row/column number?
# could write out full Gilis matrix within loop-
#- e.g. if key1.value() ===key2.value() : SumError += (p*7)
# time consumeing and prone to human error but once intially done-
#- could be copy pasted through the loop
# excel Gilis as a square (3 letter code)


#if I make an array how do I then say ‘ if codon 1 gives AA 1 and codon 2 -
# -gives AA 2 then go to array/ matrix to obtain the correct value of the change ?

SumError=()
# insert every error cost (after every full pass of the loop)into SumError
# at end of code print(SumError) to get error cost
# print(SumError/64) to compare to novozhilov?
# end every pass of a legtimate codon comparison  with SumError += (p*matrixvalue)
#for pass of loop where codons differing by more then one base SumError += 0

p=1
#in this case p is equa to p(c|c')
# once the the base position in two codons with a single differing base is found-
#-then within the loop p=1/N or 0.5/N etc to suit situation-
#- no need to set p for codn differing by 0,2,or 3 bases just SumError +=0
#p(c|c') can then be implimentented during SumError addition (SumError +=(p*matrix value))

f=1
#not neseerary for novozhilov result comparison.
# for goodarzi result comparison sumError +=(((p(a(c)/n(a(c))*f)*(p*matrixvalue))
