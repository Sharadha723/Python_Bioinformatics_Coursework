# Write a Python program to determine whether or not a DNA sequence consists of
# a (integer) number of (perfect) "tandem" repeats.
# Test it on sequences:
# AAAAAAAAAAAAAAAA
# CACACACACACACAC
# ATTCGATTCGATTCG
# GTAGTAGTAGTAGTA
# TCAGTCACTCACTCAG
# Hint: Is the sequence the same as many (how many?) repetitions of its
# first character? 
# Hint: Is the sequence the same as many (how many?) repetitions of its
# first two characters?

# input sequence
# sequence = "AAAAAAAAAAAAAAAAAA"
# sequence = "CACACACACACACAC"
# sequence = "ATTCGATTCGATTCG"
# sequence = "GTAGTAGTAGTAGTA"
# sequence = "TCAGTCACTCACTCAG"

sequence = "atgatgatg"

# printing input sequence
print("Given sequence is:", sequence)

# Creating a new function that checks for tandem repeats
def tandem_repeat_check(seq):
	half_seq = len(seq)//2
	for i in range(1,half_seq+1):
		if len(seq) % i == 0:
			tandem_repeat = seq[:i]
			if tandem_repeat * (len(seq)//i) == seq:
				positive = "Sequence contains tandem repeats"
				return positive
	negative = "Sequence does not contain tandem repeats"
	return negative

# Printing the result
print(tandem_repeat_check(sequence))
