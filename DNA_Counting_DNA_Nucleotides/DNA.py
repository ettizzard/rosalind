#!/usr/bin/python3

with open("rosalind_dna.txt", "r") as dataset:
    
    seq = dataset.read()

    print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))
