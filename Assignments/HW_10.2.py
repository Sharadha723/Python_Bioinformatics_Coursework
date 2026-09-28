# Exrcise 10.2 Sarada Giridharan

# Write a program to compute and output the frequency of each nucleotide in a DNA sequence using a dictionary (see lec. 9).
# Output the frequencies in most-occurrences to least-occurrences order.

# Importing necessary module for getting file from command line
import sys

# Check user input
if len(sys.argv) < 2:
	print("Please give sequence file")
	sys.exit()

# Getting sequence from command line, opening and reading the given sequence file
seq_file = sys.argv[1]
seq_file = open(seq_file)
seq_file = seq_file.upper() #converting to uppercase to avoid error
seq_file = ''.join(seq_file.read().split())
seqlen = len(seq_file)

# Using dictionary, we compute the frequency of each nucleotide
count = {}
for nuc in seq_file:
	if nuc not in count:
		count[nuc] = 1
	else:
		count[nuc] = count[nuc] + 1


# We sort the values and then reverse the sorting to get the descending order
sorted_val = sorted(count.items(),key=lambda items: items[1])
desc_sorted_val = reversed(sorted_val)


# output results for each nucleotide
for nuc, freq in desc_sorted_val:
	print(nuc, "Frequency:", round(100*freq/seqlen,2), "%")
