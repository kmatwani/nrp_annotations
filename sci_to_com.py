# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:10:59 2021

@author: kmatw
"""

# open and read file contents 
import sys
from collections import defaultdict
import csv

# open and read file contents
desc_file = open(sys.argv[1], 'r')
seq_file = open(sys.argv[2], 'r')
input = 1 

def sci_to_com(desc_file, seq_file):
	
    	# Read csv file and open a list to save headers in 
	reader = csv.reader(desc_file)
	headerlist = []
	headerlist2 = []
	seqlist = []
    
	#use rows to create a dictionary (key will be the scientific name, value common name). 
	com_dict = {}
	for row in reader:
		com_dict[row[0]] = row[1]
  for line in seq_file:
        if line.startswith('>'):
            headerlist.append(line)
        else:
            seqlist.append(line)

    for header in headerlist:
        first_header = header.split('[')[0]
        sci_name = header.split('[')[1]
        sci_name2 = header.split(']')[0]
        if sci_name2 in com_dict.keys():
            headerlist2.append('first_header' + '[' + str(com_dict[sci_name2]) + ']')
        else:
            headerlist.append(header)
	print(headerlist2)

sci_to_com(x, y)


TestFile = "vegfa_ex78_1000ish.txt"
f1 = open(TestFile, "r")
f2 = open('headersvegf_final3.txt', 'w')
titlelist = []
seqlist = []
res = []
line = f1.readline()
for line in f1:
    if line.startswith(">"):
        titlelist.append(line)
    else:
      seqlist.append(line)
for test_str in titlelist: 
        brack = test_str.split(']')
        splitwords = brack[0] 
        temp = splitwords.split('[')
        res = []
        for word in temp: 
            res.append(desc2.get(word, word))
        res = ' '.join(res)
        print(res)
    # printing result  
        f2.write(str(res) + "\n")  
f1.close()
f2.close()

f3 = (open('headersvegf_final3.txt', 'r'))  
f4 =(open('com_vegf78_desc.txt', 'a'))

headerlist = []
for line in f3:
    headerlist.append(line)
for i in range(len(headerlist)):
    f4.write(headerlist[i] + seqlist[i])
f3.close
f4.close


    
