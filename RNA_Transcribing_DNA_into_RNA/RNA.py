#!usr/bin/python3

with open("/workspaces/rosalind/RNA_Transcribing_DNA_into_RNA/rosalind_rna.txt", "r") as dataset:
    
    DNAseq = dataset.read()
    
    RNAseq = DNAseq.replace("T", "U")
            
    print(RNAseq)