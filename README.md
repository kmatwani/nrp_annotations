# nrp_annotations

extractHitID: 
Extracts sequence ID from the FASTA file and creates a text file with the identifier and the respective domain name.
Input: extractHitID.py domain_name filename

merge_ids:
Combines the sequence IDs and their respective domains for upto 4 files (input would be the above text file). 
Input: merge_ids.py file1 file2 file3

combined_seqs1:
Combines sequences from upto 4 FASTA files and removes duplicates. Mandatory to enter 2 filenames. 
