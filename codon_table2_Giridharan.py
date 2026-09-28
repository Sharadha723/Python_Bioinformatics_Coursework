class codon_table2_Giridharan:
    def __init__(self):
        self.table = {}

    def read(self,filename):
        f = open(filename)
        data = {}
        for l in f:
            sl = l.split()
            key = sl[0]
            value = sl[2]
            data[key] = value
        f.close()
        
        b1 = data['Base1']
        b2 = data['Base2']
        b3 = data['Base3']
        aa = data['AAs']
        st = data['Starts']
        
        self.table = {} 
        n = len(aa)
        for i in range(n):
            codon = b1[i] + b2[i] + b3[i]
            isInit = (st[i] == 'M')
            self.table[codon] = (aa[i],isInit)
        return self.table
    def amino_acid(self,codon):
        if codon in self.table:
            aa = self.table.get(codon)[0]
        else:
            aa = 'X'
        return aa
    def is_init(self,codon):
        if codon in self.table:
            result = self.table.get(codon)[1]
        else:
            result = False
        return result
    def get_ambig_aa(self,codon):
        aas = set()
        for n3 in 'ACGT':
            codon1 = codon[:2]+n3
            if codon1 in self.table:
                aas.add(self.table[codon1])
        if len(aas) != 1:
            return 'x'
        return aas.pop().lower()
    def startswith_init(self,seq):
        start_codon = seq[:3]
        if self.is_init(start_codon):
            result = "Starts with an initiation codon"
        else:
            result = "Does NOT start with an initiation codon"
    def translate(self,seq,frame):
        aalist = []
        for i in range(frame-1,len(seq),3):
            codon = seq[i:i+3]
            if 'N' in codon:
                aa = self.get_ambig_aa(codon)
            else:
                aa = self.amino_acid(codon)
            aalist.append(aa)
        aaseq = ''.join(aalist)
        return aaseq
