# Exercise 8.1 Sarada Giridharan

# Using just the concepts introduced so far, find as many (different!) ways as possible to code DNA reverse complement (at least 3!)
# You may use any built-in function or string or list method.
# You may use only basic data-types and lists and dictionaries.
# Compare and critique each technique for robustness, speed, and correctness.

# METHOD 1 - Data dictionary

# input sequence
seq = 'ATG'

# Complement dictionary
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# Reverse complement function
def revcomp(seq):
	seq = seq.upper()
	revseq = ""
	for n in seq:
		revseq = complement[n] + revseq
	return revseq

# output result
print ("Reverse complement of sequence using Method 1:", revcomp(seq))


# METHOD 2 - reversed function and join() method

# Modifying complement function
def Complementseq(nuc):
	nuc = nuc.upper()
	nucleotides = 'ACGT'
	complements = 'TGCA'
	comp = ""
	for nuc in seq:
		i = nucleotides.find(nuc)
		if i >= 0:
			comp = comp + complements[i]
		else:
			comp = nuc
	return comp


# Reversing the sequence using join and reversed function	
reversedseq = ''.join(reversed(Complementseq(seq)))

# Output result
print("Reverse complement of sequence using Method 2:",reversedseq)


# METHOD 3 - Lists

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

# Function to get reverse complement of sequence using list instead of string variable
def reverseComplement(seq):
    newseq = []
    for nuc in reversed(seq):
        newseq.append(complement(nuc))
    return ''.join(newseq)

# Output results
print("Reverse complement of sequence using Method 3:",reverseComplement(seq))
	
		
# METHOD 4 - IDEAL METHOD

# Complement dictionary
complement2 = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# Function with error message
def reverseComplement2(seq):
	newseq = []
	for nuc in reversed(seq):
		if nuc not in complement2:
			print ("Invalid nucleotide given")
		else: 
			newseq.append(complement2[nuc])
	return ''.join(newseq)

# output result
print ("Reverse complement of sequence using IDEAL method:", reverseComplement2(seq))

	

