# -*- coding: utf-8 -*-
"""

Program:    combined_seqs1.py
File:       combined_seqs1.py 

Version:    v2.0
Created on: Fri Mar 12 2021 10:16:55
Edited on:  Wed Apr 27 2022
Other edits:Mar 15, Mar 16

Author:     Khushboo Matwani

------------------------------------------------------------------------------------

Description:

Uses the merge_ids output file and FASTA files from different protein domain searches to 
create a new FASTA file with redundant sequences removed. The function cannot change headers.   

Inputs:

Files in a FASTA format (up to 4). 



"""

## making a dictionary from a FASTA help from  
##https://stackoverflow.com/questions/35635709/how-do-i-make-a-dictionary-out-of-a-collection-of-fasta


from collections import defaultdict
import sys 


def combined_seqs(file1, file2, file3 = 0 , file4 = 0):
## file1 used to make the dictionary
    file1 = open(sys.argv[1], 'r')

## files 2-4 would be used to add to the dict using a for loop 

    file2 = open(sys.argv[2], 'r')


## dictionary using file1 (key is the identifier, value is the sequence)
## headerlist1 used to save headers to create the new FASTA
    
    seq_dict = defaultdict(str)
    headerlist = []

    for line in file1:
        if line[0] == '>': 
            line_i = line.split()
            line_id = line_i[0]
            headerlist.append(line)
            key = line_id.strip('\n')
        else:
            seq_dict[key] += line.strip('\n')

## for loop to create new dictionaries using each file:
## new headerlist for the additional files
            
    headerlist2 = []   
    seq_dict2 = defaultdict(str)  
    seq_dict5 = {}
    for line in file2:
        if line[0] == '>':
            line_j = line.split()
            line_jd = line_j[0]
            headerlist2.append(line)
            key_2 = line_jd.strip('\n')
        else:
            seq_dict2[key_2] += line.strip('\n')


    if(len(sys.argv) > 3):
        seq_dict3 = defaultdict(str)  
        file3 = open(sys.argv[3], 'r')       
        seq_dict3 = defaultdict(str)
        for line in file3:
            if line[0] == '>':
                line_j = line.split()
                line_jd = line_j[0]
                headerlist2.append(line)
                key_3 = line_jd.strip('\n')
            else:
                seq_dict3[key_3] += line.strip('\n')
    else:
        key_3 = ''
        seq_dict3 = {}
    
    if(len(sys.argv) > 4):
        file4 = open(sys.argv[4], 'r')
        seq_dict4 = defaultdict(str)  
        for line in file4:
            if line[0] == '>':
                line_j = line.split()
                line_jd = line_j[0]
                headerlist2.append(line)
                key_4 = line_jd.strip('\n')
            else:
                seq_dict4[key_4] += line.strip('\n')
    else:
        key_4 = ''
        seq_dict4 = {}
        

## new dictionary with all identifiers and sequences        
                            
    seq_dict5.update(seq_dict)
    seq_dict5.update(seq_dict2)
    seq_dict5.update(seq_dict3)
    seq_dict5.update(seq_dict5)

## final headerlist with no duplicates     
    headerlist3 = (headerlist + list(set(headerlist2) - set(headerlist)))   
         
## final printing step using headerlist and seq_dict5
    for i in headerlist3:
        i_id = i.split()
        identifier = i_id[0]
        if identifier in seq_dict5:
            print(i + seq_dict5[identifier])




combined_seqs('file1', 'file2', 'file3', 'file4')
    
                
