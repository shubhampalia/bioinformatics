#program to find reverse complement of a given DNA sequence
dict = {    "A" : "T",    "T" : "A",    "G" : "C",    "C" : "G"}
f = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"

def reverse(sequence):
    reverse = " "
    for i in sequence:
        reverse = i + reverse
    return reverse    

def complement(sequence):
    complement = " "
    for j in sequence:
        complement= complement + dict.get(j)
    return complement

c = complement(f)
rev_complement = reverse(c)
print(rev_complement)
