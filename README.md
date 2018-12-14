# Modelling Code Robustness

## Masters Project 2018/19

please put a brief description of the project here.
make a ocde robustenss model based on goodarzi et al 2004.
To run Rob's "main.py" script:

```bash
$ pipenv install
$ pipenv shell
$ python main.py

```
to do list:
understand the p(c\c') = 1. what is N?
N is the sum of p(c|c') numerators ( 1 for a third base chnage 0.5 for 2nd base transition etc)
therfore need to make a function that runs through codon comparisons and sums the p(c|c') values 
not nesessacary for function to returh gilis values 
after executeing the N function then run gilis compariosn mutiplying the gilis values by th nesacary value over N

 five step plan to code robutness tests:
. define the gilis matrix
.define a function to get N and implement p(c|c')
. implement the effect of amino acid frequency and number of synomyous codons
. introduce stop codon mistranslation effect
. introduce f(c) (hopefully)














