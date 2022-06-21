# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:32:51 2021

@author: kmatw
"""

#!/usr/bin/python3

import sys

"""
Function to process and output the data. Takes a FASTA header and the 
sequence; strips out any insertion characters and prints the header and
sequence
"""
def Process(header, sbjct):
    print(header)
    sbjct = sbjct.replace("-", "")
    print(sbjct)


"""
Main program
"""

# Get the filename from the command line
filename = sys.argv[1]

# Open the file for reading
fp = open(filename, "r")

gotSequence  = False # Flag to indicate we have a sequence to print
inAlignments = False # Flag to indicate we are in the alignments block
sbjct        = ''    # The BLAST hit's sequence
theHeader    = ''    # FASTA header as read from the file
header       = ''    # The FASTA header with Range info added
rangeOK     = False # flag to indicate specific length to print 

for line in fp:
    line = line.rstrip()

    if(line[0:10] == "Alignments"):
        inAlignments = True
    elif(line[0:11] == 'Sequence ID'):
        test = line.split()
        fields1 = test[2]
    elif(line[0:5] == "Range"):    
        if(gotSequence and rangeOK):
            Process(header, sbjct)
            gotSequence  = False
        fields = line.split(' ')
        head = ('Range: ' + str(fields[2]) + ' ' + str(fields[3]) + ' ' + str(fields[4])) 
        rangeOK = True
        header = '>' + fields1 + ' ' + theHeader + ' ' + head
        sbjct  = ''

    elif(inAlignments and (line[0:1] == ">")):
        if(gotSequence and rangeOK):
            Process(header, sbjct)
            gotSequence = False
        fields2 = line.split('>')
        theHeader = fields2[1]
        header = theHeader
        sbjct     = ''
        
    elif(inAlignments and (line[0:5] == "Sbjct")):
        fields       = line.split()
        sbjct       += fields[2]
        gotSequence  = True

if(gotSequence and rangeOK):
    Process(header, sbjct)
