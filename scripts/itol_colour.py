# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:05:30 2021

@author: kmatw
"""


import sys
print('''TREE_COLORS
SEPARATOR TAB
DATA''')

# Colours in hexadecimal
# Blue	0000FF
#Red	FF0000
#Yellow	FFFF00
#Green	00FF00
#Black	000000

colour_class = {40674: '#0000FF', 8504: '#FFFF00', 8292: '#00FF00', 8782: '#FF0000', 7898: '#FF00FF', 2682553: '#A52A2A', 9443: "#aaaaff", 6073: "#FFA500", 7777: "#800080", 6656: "blech", 6447: "blech", 7586 : "blech", 6073 : "blech" }

class_file = open('taxonomies_full.txt', 'r')

lineages_taxid = {}

for line in class_file:
    line = line.lower()
    name = line.split('\t')[0].rstrip()
    lineage = line.split('\t')[1]
    lineages_taxid[name] = lineage
    

primate = 9443
classes = [40674, 8504, 8292, 8782, 7898, 2682553, 6073, 7777, 6656, 6447, 7586]

f1 = open(sys.argv[1], 'r')

punctuation_mark = [':', ',', '.', '[', ']', '(', ' ', ]
j = 0


for line in f1:
    if line.startswith('>'):
        species_name = line.split('[')[1].split(']')[0].lower()
        specific_lineage = lineages_taxid[species_name]
        taxids = specific_lineage.split()
        for i in punctuation_mark:
            line = line.replace('>', '')
            if i in line:
                line = line.replace(i, '-')
                j += 1
                line_no2 = line.replace(';', '').replace(')', '-')
                line_no3 = line_no2.replace('--', '-')
            
        for i in taxids:
            if int(i) in classes:
                print(line_no3.rstrip() + "\tlabel_background\t" + colour_class[int(i)])
        for i in taxids:    
            if int(i) == primate:
                print(line_no3.rstrip() + "\tlabel_background\t" + colour_class[int(i)])

            
                                          
        
        
        
        
        
        
    