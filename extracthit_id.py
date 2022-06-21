# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:53:02 2021
Created on
Program:    ExtractHitID.py
File:       extracthit_id.py

Version:    v2.0
Created on: Thu Mar 11 2021 16:53:02 
Edited on:  Thu Apr 27 2022
Function:   Extracts identfier from a FASTA files and adds the domain name specified by the user.

Author:     Khushboo Matwani
-----------------------------------------------------------------------------------------------------

Description:

Uses the start of each header line (>) to specify where the ID is. The line is separated based on spaces. The > is dropped. 

Inputs:

domain name and FASTA file 

python extracthit_id.py domain_name file.txt
"""

import sys 

#command line inputs x should be the domain name; y should be the filename (FASTA format)
x = sys.argv[1]
y = sys.argv[2] 
#function identifies the header, separates it based on spaces, and returns the id and the domain name. 
def extractHitID(domain_name, hit_file):
    
    f1 = open(hit_file, 'r')
     
    for line in f1:
        #identify header lines
        if line.startswith('>'):
            #separate based on spaces 
            fields = line.split()
            #remove '>'
            ID = fields[0].split('>')
            #choose ID
            identifier = (ID[1])
            #print ID and domain name
            print(identifier + ' ' + domain_name)
    
           
extractHitID(x, y)
