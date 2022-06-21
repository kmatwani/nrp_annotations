# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:48:37 2021

@author: kmatw
"""

#!/usr/bin/python3
# ----------------------------------------------------------------------
# Simple program to create an iTol colouring annotation file based on
# the presence of the words cyt, MAM and a1b1 in the FASTA header
#
# 26.03.21 Original By: ACRM
# ----------------------------------------------------------------------
import sys
import re

# ----------------------------------------------------------------------
def print_header():
    """
    Inputs: none
    Returns: none

    Prints the iTol annotation header

    26.03.21 Original   By: ACRM
    """
    print('''TREE_COLORS
SEPARATOR TAB
DATA''')

# ----------------------------------------------------------------------
def write_annotation(line):
    """
    Inputs:  line     A FASTA header line
    Returns: none

    Does the actual work of writing an annotation line based on a 
    FASTA header line

    26.03.21 Original   By: ACRM
    """

    line = line.rstrip()  # Remove linefeed
    line = line[1:]       # Remove the >

    # look for the domain annotation between {}
    match = re.search('{(.+?)}', line)
    r = '00'
    g = '00'
    b = '00'
    # update R/G/B based on which domains are present
    if match:
        annotation = match.group(1)
        if 'cyt' in annotation:
            r = 'FF'
        if 'MAM' in annotation:
            g = 'FF'
        if 'a1b2' in annotation:
            b = 'FF'
        colour = r + g + b
        if colour == 'FFFFFF':
            colour = '000000'
        # Write the annotation line
        annotation = (line + "\tbranch\t#" + colour+"\tnormal\t1")
        print(annotation.rstrip())

# ---------------------------- Main program ----------------------------
# Obtain the FASTA file from the command line
fasta_file = sys.argv[1];

# Print the iTol header
print_header()

##removing additional characters:



# Process each FASTA header line
with open(fasta_file, 'r') as infile:
    for line in infile:
        if line.startswith('>'):
            line_dash = line.replace(':', '-').replace(',', '-').replace('.', '-').replace('[', '-').replace(']', '-').replace('(', '-').replace(')', '').replace(' ', '-').replace(';', '')
            line_final = line_dash.replace('--', '-')
            line_strip = line_final.rstrip()
            write_annotation(line_strip)
            
            
            
            
            
