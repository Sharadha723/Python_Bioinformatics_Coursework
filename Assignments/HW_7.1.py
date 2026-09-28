# Exercise 7.1 Sarada Giridharan

# Write a command-line program for computing the reverse complement of primer pairs:
# Primer pairs are listed in a file, one per line.
# Forward and reverse primers on each line are separated by a space. Ignore anything after the first two space separated “words” on each line.
# e.g. Example input file: here
# Print the reverse complement of each primer of the pair in the same format as the input file. 
# Hint: Use open(…).read() [with no arguments]to read the entire contents of the file into a string…

# Getting file from command line
import sys
seq_file = sys.argv[1]

# Open file, read contents,and convert to uppercase
input_seq = open(seq_file).read()
input_seq = input_seq.upper()

# Function for getting complement of sequence
def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Function to get reverse complement of sequence 
def reverseComplement(seq):
	seq = seq.upper()
	revseq = ""
	for n in seq:
		revseq = complement(n) + revseq
	return revseq
 

# Getting individual sequences from each line and their reverse complement
for lines in input_seq.splitlines():
    no_primers = lines.split()
    forward_p = reverseComplement(no_primers[0])
    reverse_p = reverseComplement(no_primers[1])
    print(forward_p, reverse_p)



