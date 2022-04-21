# -*- coding: utf-8 -*-
"""
Program:    merge_ids.py
File:       merge_ids.py

Version:    v2.0
Created on: Thu Mar 11 2021
Edited on:  Thu Apr 21 2022
Function:   Adds complete domain information of a protein from varrious files.

Author:     Khushboo Matwani

------------------------------------------------------------------------------- 

Description:    

Makes a dictionary with IDs and domain names using 1 file and                   compares the contents of the other ones to add/append entries in                the dictionary.

Inputs:     

Text files that contain a table of the IDs and one of the domains present in the protein (Max 4). 

e.g.

XP123456    SH3
XP789101    SH3


"""

import sys 

    ## files 3 and 4 are optional
def merge_ids(file1, file2, file3 = '', file4 = ''):

    ## opens file1 to create a dictonary (key = id, value = domain name)
    f1 = sys.argv[1]
    filename = open(f1, 'r')

    ## save files 2-4 as a list and open later using a for loop
    filenames = []
    f2 = sys.argv[2]
    file2 = f2
    filenames.append(file2)

    ##If values present for files 3 and 4, then they are added to the list
    if(len(sys.argv) > 3):
        f3 = sys.argv[3]
        filenames.append(f3)
    if(len(sys.argv) > 4):
        f4 = sys.argv[4]
        filenames.append(f4)

    ## dictionary using file1 
    head1 = {}

    for line in filename:
        split1 = line.split(' ')
        f1_domain = str(split1[1]).rstrip()
        id_1 = split1[0] 
        head1[id_1] = (f1_domain)

    ## for loop for opening files 2-4 and appending/adding to the dictionary
    for i in filenames:
        openfile = open(i, 'r')

        id_2 = []    
        for line in openfile: 
            split2 = line.split(' ')
            f2_domain = str(split2[1]).rstrip()
            id_2.append(split2[0])
        ## using ids to add/append to the dictionary      
        for key in id_2:
            if key in head1:
                head1[key] = (head1[key]) + ',' + f2_domain
            else: 
                head1[key] = f2_domain 

    for key in head1:
        print(str(key) + ' ' + str({head1[key]}))
    
merge_ids('file1', 'file2', 'file3', 'file4')
    
## help from https://stackoverflow.com/questions/41825868/update-python-dictionary-add-another-value-to-existing-key
