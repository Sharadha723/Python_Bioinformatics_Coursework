# Write a python program to print out the codon for Methionine (aka the start codon) backwards in lower-case symbols.
# Start with Methionine represented as string variable codon=“ATG”


start_codon = "ATG"
start_codon_lower = start_codon.lower()
print("Start codon in lowercase :", start_codon_lower)
first_nt = start_codon_lower[0]
second_nt = start_codon_lower[1]
third_nt = start_codon_lower[2]
start_codon_reverse= third_nt + second_nt + first_nt
print("Lowercase start codon in reverse:", start_codon_reverse)
