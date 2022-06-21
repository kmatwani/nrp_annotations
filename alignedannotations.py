# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:40 2021

@author: kmatw
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:55:08 2021

@author: kmatw
"""
from collections import defaultdict
import sys 

def aligned_ann(domain_merge, seqs_file): 

## important that the sequence file is in a BLAST aligned sequences format    
    domain_merge = open(sys.argv[1], 'r')
    seqs_file = open(sys.argv[2], 'r')

    dom_id = {} 
    for line in domain_merge:
        id_ = line.split('{')
        key = str('>' + id_[0])
        value = str('{'+ id_[1])
        dom_id[key] = value
    seq_dict = defaultdict(str)    
    headerlist = []      
    for line in seqs_file: 
        if line[0] == '>': 
            line_i = line.split()
            line_id = (str(line_i[0]) + ' ')
            headerlist.append(line)
            key = line_id
        else:
            seq_dict[key] += line.strip('\n') 

    headerlist2 = []
    for i in headerlist:
        id_head = i.split()
        id_head1 = str(id_head[0]).split(':')
        identifier = (id_head1[0] + ' ')
        if identifier in dom_id:
            get_id = dom_id.get(identifier)
            new_header = (i.strip('\n') + get_id)
            headerlist2.append(new_header)


    for i in headerlist2:
            i_id = i.split()
            id_seq = (str(i_id[0]) + ' ')
            if id_seq in seq_dict:
                print(i + seq_dict[id_seq] )

aligned_ann('domain_merge', 'seqs_file')
