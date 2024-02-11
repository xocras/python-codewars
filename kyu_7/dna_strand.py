# Complementary DNA

# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def dna_strand(dna):
    reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(reverse[x] for x in dna)

# def dna_strand(dna):
#     return dna.translate(str.maketrans("ATGC", "TACG"))
