# Exercise 8.2 Sarada Giridharan

# Write a program that takes a codon table file (such as standard.code from the lecture) and a file containing nucleotide sequence (anthrax_sasp.nuc) as command-line arguments, and outputs the amino-acid sequence.
# Modify your program to indicate whether or not the initial codon is consistent with the codon table's start codons.
# Use NCBI's taxonomy resource to look up and download the correct codon table for the anthrax bacterium. Re-run your program using the correct codon table. Is the initial codon of the anthrax SASP gene a valid translation start site? – use init dictionary

# Getting files from command line
import sys
table = sys.argv[1]
nuc_file = sys.argv[2]

# Opening and reading the codon table
f = open(table)
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
f.close()

# Assigning proper variables to recognise and use the values in codon table
b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

# Creating dictionaries to get translated amino acid sequences
codons = {}
init = {}
n = len(aa)

for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = st[i] == 'M'
 
# Opening and reading the sequence file   
f2 = open(nuc_file)
seq = ''.join(f2.read().split())
seq = seq.upper()
f2.close()

seqlen = len(seq)
aaseq = []

# Taking every 3 nucleotides from given sequence and getting their counterpart amino acid from table
for i in range(0,seqlen,3):
    codon = seq[i:i+3]
    if len(codon) == 3:
        aa = codons[codon]
        aaseq.append(aa)
print("Amino acid sequence:",''.join(aaseq))

# Checking the start codon - if it is consistent with the one from table
start_seq = seq[0:3]
if init.get(start_seq):
	print("True")
else:
	print("False")






