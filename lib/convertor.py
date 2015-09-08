# -*- coding:utf8 -*-  

import xlrd, os, csv, sys, re

pattern = re.compile(r'[^a-zA-Z0-9-]')

def convertfile(filename, output, recoders, today):

	filedata = {}	# all data in the file
	mydir = '..'+os.sep+'input'+os.sep
	workbook = xlrd.open_workbook(mydir+filename)
	for booksheet in workbook.sheets():
		for row in range(1, booksheet.nrows):
			actail = str(booksheet.cell(row, 0).value)[0:6]
			if not actail: continue
			if '.' in actail: actail = 'B-' + actail[0:4]
			if '-' not in actail: actail = 'B-' + actail[1:5]
			if filedata.has_key(actail):
				filedata[actail]['frame'] = str(booksheet.cell(row, 6).value)
				continue
			else:
				airline = filename[:-5].encode('utf-8')
				rowdict = {'ac':actail, 'date':today, 'airline':airline}
				switch = {1:'type', 2:'engine', 3:'fdr', 4:'cvr', 5:'qar', 6:'frame', 7:'dar'}
				
				for col in range(1, booksheet.ncols):
					colvalue = str(booksheet.cell(row, col).value).replace('\n', '')
					colvalue = re.sub(pattern, '', colvalue)
					rowdict[switch[col]] = colvalue

				filedata[actail] = rowdict

	for rowdict in filedata.values():
		airrow = [''] * 51
		airrow[0] = rowdict['ac']
		airrow[1] = rowdict['date']
		airrow[2] = rowdict['airline']
		airrow[3] = rowdict['type']
		airrow[7] = 1
		qarinfo = recoders['qar'].get(rowdict.get('qar'))
		if qarinfo:
			airrow[8] = int(qarinfo) - 1 	# maint recoder的索引从0开始
		airrow[9] = recoders['qar'].get(rowdict.get('dar'))
		fdrinfo = recoders['fdr'].get(rowdict.get('fdr'))
		if fdrinfo:
			airrow[10] = 1000 + int(fdrinfo)		# crash recoder的索引从1001开始
		airrow[32] = rowdict['engine']		# Engine 1 type
		output.writerow(airrow)