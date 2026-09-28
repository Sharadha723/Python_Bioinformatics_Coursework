# Exercise 5.2 Sarada Giridharan

# Write a program to test whether a PCR primer is a reverse complement palindrome.
# Such a primer might fold and self-hybridize!
# Test your program on at least the following primers: - does the first half match the reverse complement of the second half – there is a subtlety you should discover
# TTGAGTAGACGCGTCTACTCAA
# TTGAGTAGACGTCGTCTACTCAA
# ATATATATATATATAT
# ATCTATATATATGTAT

# assign primer sequences to variables
primer1 = "TTGAGTAGACGCGTCTACTCAA"
primer2 = "TTGAGTAGACGTCGTCTACTCAA"
primer3 = "ATATATATATATATAT"
primer4 = "ATCTATATATATGTAT"
primer5 = "AATTT"

# creating function to compute complement
def complement(nuc):
	nucleotides = "ATGCatgc"
	complements = "TACGtacg"
	i = nucleotides.find(nuc)
	if i >= 0:
		comp = complements[i]
	else:
		comp = nuc
	return comp

# creating function to compute reverse complement
def ReverseComplement(seq):
	seq = seq.upper()
	newseq = ""
	for nuc in seq:
		newseq = complement(nuc) + newseq
	return newseq

# creating function to check if the sequence is a reverse complement palindrome
def Palindrome(seq):
	length = len(seq)//2
	if len(seq) % 2 == 0:
		if ReverseComplement(seq[0:length]) == seq[length:]:
			output = True
		else:
			output = False
	else:
		if ReverseComplement (seq[0:length]) == seq[length+1:]:
			output = True
		else:
			output = False
	return output

# output results
print("Primer 1:", Palindrome(primer1))
print("Primer 2:", Palindrome(primer2))
print("Primer 3:", Palindrome(primer3))
print("Primer 4:", Palindrome(primer4))
print("Primer 5:", Palindrome(primer5))
