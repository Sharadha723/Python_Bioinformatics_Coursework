# Exercise 16.1 and 17.1

# Rework the lecture, and your solutions (or mine) from the Homeworks #1 through #4, to make a MyDNAStuff module.
# Put as many useful nucleotide functions as possible into the module...

# Rework the lecture, and your solutions (or mine) from Homework #5 to make the codon_table module with functions specified in this lecture.

# Demonstrate the use of these modules to translate an amino-acid sequence in all six-frames with just a few lines of code.
# The final result should look similar to Slide 10.
# Your program should handle DNA sequence with N’s in it.

from MyDNAStuff_Giridharan import *
from codon_table_Giridharan import *
import sys

# check if arguments are properly given
if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

# get table and sequence from given arguments using function from modules
table = read_codons_from_filename(sys.argv[1])
seq = readseq(sys.argv[2])

# printing translated sequences for 3 forward frames
for frame in (1,2,3):
  print("Frame",frame,"(forward):",translate(table,seq,frame))

# reverse complement sequence
rev_comp_seq = revcomp(seq)

# translating reverse complement sequence for reverse 3 frames
for frame in (1,2,3):
    print("Frame",frame,"(reverse):",translate(table,rev_comp_seq,frame))



