# Write a python program to find the position and the translation frame
#(1, 2, or 3) of the first start-codon in the DNA sequence:
#	     gcatcacgttatgtcgactctgtgtggcgtctgctggg

start_codon = "atg"
sample_seq = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"
position_start = sample_seq.find(start_codon)
print("Position of start codon in the given sequence :", position_start)
frame_no = (position_start % 3) +1
print("Translation frame of start codon in the given sequence :",frame_no)
