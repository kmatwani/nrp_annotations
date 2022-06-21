# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:17:10 2021

@author: kmatw
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:56:44 2021

@author: kmatw
"""
from collections import defaultdict
import sys 

keywords = ['nrp', 'neuropilin', 'nrp1', 'nrp2']
def select_seq(alignment_file, query):

    seq_dict = defaultdict(str)
    query_header = []
    other_header = []
    

    alignment_file = open(sys.argv[1], 'r')

    if len(sys.argv > 2):
        query = sys.argv[2]
    else:
        query = keywords
    
    for line in alignment_file:
        if line.startswith('>'):
            header = line.lowercase()
            for i in query:
                if i in header:
                    query_header.append(header)
                else:
                    other_header.append(header)
        else:
            seq_dict[header] += line.strip("\n")
            
    
    for i in query_header:
        print(query_header + "\n" + seq_dict[i])
    
    
                    
    




                
    
 

        
        