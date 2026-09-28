# Exercise 9

# a. Modify your DNA translation program to translate in each forward frame (1,2,3)

# b. Modify your DNA translation program to translate in each reverse (complement) translation frame too.

# c. Modify your translation program to handle 'N' symbols in the third position of a codon
# If all four codons represented correspond to the same amino-acid, then output that amino-acid.
# Otherwise, output 'X'.

# importing necessary module for getting files in command line
import sys

# check there is user input
if len(sys.argv) < 3:
	print("Please provide a codon table and DNA sequence on the command line")
	sys.exit()

# Getting files from command line
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
n = len(aa)

for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    
 
# Opening and reading the sequence file   
f2 = open(nuc_file)
seq = ''.join(f2.read().split())
seq = seq.upper()
f2.close()

seqlen = len(seq)

# reverse complement function
def rev_comp(seq):
	complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
	return ''.join(complement.get(nt) for nt in reversed(seq))

# reverse complemented sequence
reverse_comp_seq = rev_comp(seq)

# Taking every 3 nucleotides from given sequence and getting their counterpart amino acid from table
def translate(frame,ntseq):
	aaseq = []
	for i in range(frame,len(ntseq),3):
		codon = ntseq[i:i+3]
		if len(codon) == 3:
			if codon[2] == 'N':
				aa = handle_codon(codon)
			else: 
				aa = codons.get(codon, 'X')
			aaseq.append(aa)
	return ''.join(aaseq)


# part c - creating a handle_codon function to handle 'N' inside the sequence
def handle_codon(codon):
		possible_codon = list(codon[0]+codon[1]+base for base in 'ATCG')
		list_codon = list(codons.get(c, 'X') for c in possible_codon) 
		if list_codon[0] == list_codon[1] == list_codon[2] == list_codon[3]:
			return list_codon[0]
		else:
			return 'X'		

# printing out results
print("Amino acid sequence in frame 1:",translate(0,seq))
print("Amino acid sequence in frame 2:", translate(1,seq))
print("Amino acid sequence in frame 3:", translate(2,seq))
print("Amino acid sequence in frame -1:", translate(0,reverse_comp_seq))
print("Amino acid sequence in frame -2:", translate(1,reverse_comp_seq))
print("Amino acid sequence in frame -3:", translate(2,reverse_comp_seq))












