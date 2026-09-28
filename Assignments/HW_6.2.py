# Write a command-line program for manipulating a DNA sequence:
# DNA sequence in a file, with the filename provided on the command-line
# Manipulation command also provided on the command-line:
# Command is one of: Complement, Reverse, or ReverseComplement
# Print the DNA sequence, and the appropriate manipulation of the DNA sequence to the terminal. 

# Get file and command from command line
import sys
seq_file = sys.argv[1]
command = sys.argv[2]

# MAGIC: open file, read contents, and remove whitespace
input_seq = ''.join(open(seq_file).read().split())

# Creating function to compute complement
def complement(nuc):
    nucleotides = 'ACGTatcg'
    complements = 'TGCAtagc'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Creating function to compute reverse complement
def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# Creating function to compute reverse
def reverse(seq):
	seq = seq.upper()
	newseq = ""
	for nuc in seq:
		newseq = nuc + newseq
	return newseq

# Checking the command to give desired output
if command == "Complement" or command == "complement":
	print ("Complement of given sequence:", reverse(reverseComplement(input_seq)))
elif command == "Reverse" or command == "reverse":
	print(" Reverse of given sequence:", reverse(input_seq))
elif command == "ReverseComplement" or command == "reversecomplement":
	print("Reverse complement of given sequence:", reverseComplement(input_seq))



