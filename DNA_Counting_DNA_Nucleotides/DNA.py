#!/usr/bin/python3
with open("/workspaces/rosalind/DNA_Counting_DNA_Nucleotides/rosalind_dna.txt", "r") as dataset:
    seq = dataset.read()
    print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))
