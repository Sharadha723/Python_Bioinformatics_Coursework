#codon_table module - Sarada Giridharan

import sys

# reads the file
def read_codons_from_filename(codonfile):
    try:
        f = open(codonfile)
        data = {}
        for l in f:
            sl = l.split()
            key = sl[0]
            value = sl[2]
            data[key] = value
        f.close()

        try:
            b1 = data['Base1']
            b2 = data['Base2']
            b3 = data['Base3']
            aa = data['AAs']
            st = data['Starts']
        except KeyError:
            print("Missing key in codon table")

        codon_table = {} 
        n = len(aa)
        for i in range(n):
            codon = b1[i] + b2[i] + b3[i]
            isInit = (st[i] == 'M')
            codon_table[codon] = (aa[i],isInit)
        return codon_table
    except IOError:
        print("Cannot find sequence file")
    except FileNotFoundError:
        print("Cannot find file")
    except:
        print("Cannot read file")


# gets amino acid from table
def amino_acid(table,codon):
    try:
        aa = table.get(codon, 'X')
        return aa
    except:
        print("Cannot find amino acid in table")

# checks for initiation codon
def is_init(table,codon):
    try:
        return table.get(codon,(None,False))[1]
    except KeyError:
        print("Codon not found in dictionary")        
    

# determine amino acid with ambiguous third base
def get_ambig_aa(table,codon):
    aas = set()
    for n3 in 'ACGT':
        codon1 = codon[:2]+n3
        try:
            aas.add(table[codon1])
        except KeyError:
            print("Codon not found in table")
    if len(aas) > 1:
        return 'x'
    return aas.pop().lower()

# translating nucleotide sequence to amino acid sequence in each specified frame 
def translate(table,seq,frame):
    try:
        seq += 'N'*(frame-1)
        aalist = []
        for i in range (frame-1,len(seq),3):
            codon = seq[i:i+3]
            if codon in table:
                aa,isInit = table[codon]
            elif codon.count('N') == 1 and codon[2] == 'N':
                aa = get_ambig_aa(table,codon)
            else:
                aa = 'X'
            aalist.append(aa)
        aaseq = ''.join(aalist)
        return aaseq
    except:
        print("Unable to translate")


    
