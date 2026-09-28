# Exercise 4.1 Sarada Giridharan

# Write a Python program to compute the reverse complement of a codon
# Use my solution to Homework #1 Exercise #1 as a starting point
# Add the “complement” function of this lecture(slide 9) as provided.
# Modularize! Place the reverse complement code in a new function. 
# Call the new function with a variety of codons
# Change the complement function to handle upper and lower-case nucleotide symbols.
# Test your code with upper and lower-case codons.

# The input codon for the program
# codon = 'ATG'

# Other input values to check correctness
codon = 'atg'
# codon = 'GTA'
# codon = 'XYZ'
# codon = 'aaa'

# output the result
print("The input codon is :",codon)

# Determine the complementary nucleotide by creating a new function
def complement(nuc):
	if nuc == 'A':
	   comp = 'T'
	elif nuc == 'T':
	   comp = 'A'
	elif nuc == 'G':
	   comp = 'C'
	elif nuc == 'C':
	   comp = 'G'
	else :
	     comp = "NIL"
	return comp

# create another function to get reverse complement 
def reverse_comp(nt):
	nt = nt.upper()
	first = nt[0]
	second = nt[1]
	third = nt[2]

# using complement fuction inside a function
	comp_first = complement(first)
	comp_second = complement(second)
	comp_third = complement(third)

# using if loop to determine if input sequence is a nucleotide	
	if comp_first == "NIL" or comp_second == "NIL" or comp_third  == "NIL":
		output = "does not exist for this sequence"
		return output
	else:	
		output = comp_third + comp_second + comp_first
		return output

# printing output
print ("The reverse complement:", reverse_comp(codon))
	



