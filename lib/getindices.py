import csv, os

# inport informations about relations between recoders and indices
def get_fdr_indices(recoders):
	reader = csv.reader(file('..'+os.sep+'recoder_index'+os.sep+'fdr.csv', 'rb'), delimiter='\t')
	for line in reader:
	    recoders[line[0].strip()] = line[2].strip()
	return recoders
