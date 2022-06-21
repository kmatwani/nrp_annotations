# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:05:13 2021

@author: kmatw
"""

import sys 


filename = open(sys.argv[1], 'r')
species = []
filenames = []
number = 2
inputs = []
filenames = []
if len(sys.argv) > 2:
    inputs.append(sys.argv[number])
 
if len(sys.argv) > 3:
    inputs.append(sys.argv[3])
       


for line in filename:
    
    if line.startswith('>'):
        line = line.split('[')[1]
        line = line.split(']')[0]
        if line in species:
            continue
        else:
            species.append(line)
    

for file in inputs:
    print(file)
    filename2 = open(file, 'r')
    for line in filename2:
        if line.startswith('>'):
            line = line.split('[')[1]
            line = line.split(']')[0]
            if line in species:
                continue 
            else:
                species.append(line)
    
for i in species:
    print(str(i))