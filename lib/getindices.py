import csv, os

# inport informations about relations between recoders and indices
def get_fdr_indices(recoders):
	mydir = '..'+os.sep+'recoder_index'+os.sep
	files = os.listdir(mydir)
	for filename in files:
		reader = csv.reader(file(mydir+filename, 'rb'), delimiter='\t')
		recoderType = filename.split('.')[0]
		recoders[recoderType] = {}
		for line in reader:
			recoders[recoderType][line[0].strip()] = line[2].strip()
	return recoders
