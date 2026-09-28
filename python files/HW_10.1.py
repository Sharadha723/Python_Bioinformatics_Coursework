# Exercise 10.1 Sarada Giridharan

# Write a reverse complement function (and package it up as a program) as compactly as possible (1-2 lines), using the techniques introduced today.
# Hint: Use a dictionary for complement, reversed on the sequence, list comprehension to apply the get method of the dictionary, and the join method for strings. 

# Importing necessary module for getting files in command line
import sys

# Error message if file not given
if len(sys.argv) < 2: 
	print("Please provide a sequence file")
	sys.exit()

# Getting file from command line
seq_file = sys.argv[1]
seq_file = open(seq_file)
seq_file = ''.join(seq_file.read().split())

# Defining a reverse complement function according to instructions
def rev_comp(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(complement.get(nt, 'X') for nt in reversed(seq))

# Output results
print("reverse complement of given sequence:", rev_comp(seq_file))
