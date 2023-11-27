#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("rosalind_gc.txt") as data:

    header = []
    DNAseq = []
    seq = []
    
    for line in data:
        
        line = line.strip()
        
        if not line.startswith(">"):
#            print("Test")
            seq.append(line)
            
        
        if line.startswith(">"):
            header.append(line.strip(">"))
            if seq != []:
                seq = "".join(seq[0::])
                DNAseq.append(seq)
#                print(seq)
                seq = []

    seq = "".join(seq[0::])
    DNAseq.append(seq)
#    print(seq)
            
#    print(header)
#    print(DNAseq)
    
    highestGC = 0
    
    for entry in DNAseq:
        numGC = entry.count("G") + entry.count("C")
        length = len(entry)
        GCcontent = (numGC / length * 100)
        currentGC = GCcontent
        
        if currentGC >= highestGC:
            highestGC = currentGC
#            print(highestGC)
            highestGCstring = entry
            
    idsandseqs = dict(zip(header, DNAseq))
#    print(test)
#    print(highestGCstring)

    print(list(idsandseqs.keys())[list(idsandseqs.values()).index(highestGCstring)])
    print("{:.6f}".format(highestGC))




# In[ ]:




