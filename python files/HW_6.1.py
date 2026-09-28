# Exercise 6.1 Sarada Giridharan

# Extend your solution for Exercise 1 from Lecture 5 to get its two PCR primers from the command-line.

# forward primer sequence = CAGCACATGACGGAGGTTGT 
# reverse primer sequence = TCATCCAAATACTCCACACGC

# Assigning arguments to get sequence into variables
import sys
input_seq_1 = sys.argv[1]
input_seq_2 = sys.argv[2]

# Creating a function to compute complement
def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Creating a function to compute reverse complement
def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# output results
print("Reverse complement of sequence 1:", reverseComplement(input_seq_1))
print("Reverse complement of sequence 2:", reverseComplement(input_seq_2))



