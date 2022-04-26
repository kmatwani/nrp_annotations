# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:10:59 2021

@author: kmatw
"""

# open and read file contents 
import csv
filename = open('vegfa_desc.csv', 'r')
reader = csv.reader(filename)
f3 = open('desc_dict.txt', 'w')
#use rows to create a dictionary (key will be the scientific name, 
# value common name). 

desc2 = {}

for row in reader:
    desc2[row[0]] = row[1]
    f3.write(str(desc2))
    
filename.close()

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


    
