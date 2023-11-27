#!/usr/bin/python3

with open("rosalind_revc.txt", "r") as dataset:
    
    DNAseq = dataset.read()
    
# Need to reverse the DNA strand to begin complementary strand
    revseq = DNAseq[::-1]
    
#Now need to replace all nucleotides in reversed strand with their complementary bases. Must make replaced bases lowercase so as not to overwrite prior replacements, then return the fully capitalized string.        
    revcomp = revseq.replace("T", "a").replace("G", "c").replace("A","t").replace("C","g")
    revcomp = revcomp.upper()
        
    print(revcomp)