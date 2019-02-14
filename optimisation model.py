
# the Blastocrithidia code, for reference.

SGC={"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
    "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
    "UAU":"Tyr", "UAC":"Tyr", "UAA":"Glu", "UAG":"Glu",
    "UGU":"Cys", "UGC":"Cys", "UGA":"Trp", "UGG":"Trp",
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

# need to rearange these based on swaping in four codon blocks, then two codon blocks
#split into codon block based dictionaries 
# have dictionaires for 4 codon blocks, containing two dictinoaries for two codon blocks
# how to reassign the values to keys, and do it to dict inside dicts 
# if this works then if the values of all keys in all dicts in a dict are the same-
#-then it isn't considered for the two codon swaps
# how then to swap one dict inside a dict witha dict in another dict. keeping keys the same?
# make a dictionary with of 4 codon blocks dcitionaries, containing-
# two codon block dictionary if two codon block eligible, and just codons otherwise?
# make an array of te data, which can be swaped and then converted to a dictionary?


# alternatively work in a excel file, fisr column codons, secound AA, third a num to mark-
#- four codon block number, fourth a num to mark two codn block number
# would need to change data within file, then convert the to dictionary in python
# the dict could only include the codon and AA pairs, not numbers
# would need to be able to read into dictinary as 4 codon blocks containg two codon blocks
# then if all codons in four codon blocks have the same value ignore from two codon swaps
#theres a module called openpyxl that allows excel manipulation in python
# according to comments on the youtube video its not very good though


#will need a function that can swap values of keys in a dict or manipult file.
# regardless will need to be able to discriminate the four codon blocks 
# will also need to discrimnate the two codn blocks within fourcdon and which to avoid
# for both process will need to ignore the Blastocrithidia four and two blocks
# in excel mark Blasto four/two codon block with specific number or value?
# in dictionries need to put in sub dictinary, but if I'm doing that-
#- anyway how des that differentiate it?
# regard less of set up, assign a 0 or 1 tocodn four/two block to define if swapped

























