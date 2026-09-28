# Exercise 5.1 Sarada Giridharan

# Use PrimerBank (“google PrimerBank”) to look up PCR primers for your favorite gene
# Use Search By: “NCBI Gene Symbol”, Species: “Human” to find PCR primers for your gene. 
# Write a program to compute the reverse complement sequence of both the forward and reverse primer (in one program).

# taking TP53 primer sequences from Primer Bank
forward_p = "CAGCACATGACGGAGGTTGT"
reverse_p = "TCATCCAAATACTCCACACGC"

# defining a new function for getting complement of sequence
def complement(nuc):
    nucleotides = 'ACGTatcg'
    complements = 'TGCAtagc'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# creating a new function for getting reverse complement 
def reverseComplement(seq):
    seq = seq.upper() 
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# output results
print("Reverse complement of forward primer of TP53:", reverseComplement(forward_p))

print ("Reverse complement of reverse primer of TP53:", reverseComplement(reverse_p))
