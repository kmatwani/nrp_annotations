# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:53:02 2021

@author: kmatw
"""

import sys 

x = sys.argv[1]
y = sys.argv[2] 

def extractHitID(domain_name, hit_file):
    
    f1 = open(hit_file, 'r')
     
    for line in f1:
        if line.startswith('>'):
            fields = line.split()
            ID = fields[0].split('>')
            identifier = (ID[1])
            print(identifier + ' ' + domain_name)
    
           
extractHitID(x, y)
