# -*- coding:utf8 -*-  

import xlrd, os, csv, sys

def convertfile(filename, output, recoders, today):

	filedata = {}	# all data in the file
	workbook = xlrd.open_workbook('..'+os.sep+'input'+os.sep+filename)
	for booksheet in workbook.sheets():
		for row in range(1, booksheet.nrows):
			actail = str(booksheet.cell(row, 0).value)[0:6]
			if not actail: continue
			if '.' in actail: actail = 'B-' + actail[0:4]
			if '-' not in actail: actail = 'B-' + actail[1:4]

			if filedata.has_key(actail):
				filedata[actail]['frame'] = str(booksheet.cell(row, 6).value)
				continue
			else:
				airline = filename[:-5].encode('utf-8')
				rowdict = {'ac':actail, 'date':today, 'airline':airline}
				# switch = {
				# 		1: lambda x: rowdict['type'] = x,
				# 	 	2: lambda x: rowdict['engine'] = x,
				# 	 	3: lambda x: rowdict['fdr'] = x,
				# 	 	4: lambda x: rowdict['cvr'] = x,
				# 	 	5: lambda x: rowdict['qar'] = x,
				# 	}
				
				for col in range(1, booksheet.ncols):
					colvalue = str(booksheet.cell(row, col).value).replace('\n', '')
					colvalue = colvalue.replace('\r', '').strip()
					# switch[col](colvalue)
					if col == 1:
						rowdict['type'] = colvalue
					if col == 2:
						rowdict['engine'] = colvalue
					if col == 3:
						rowdict['fdr'] = colvalue
					if col == 4:
						rowdict['cvr'] = colvalue
					if col == 5:
						rowdict['qar'] = colvalue

				filedata[actail] = rowdict

	for row in filedata.values():
		airrow = [''] * 51
		airrow[0] = row['ac']
		airrow[1] = row['date']
		airrow[2] = row['airline']
		airrow[3] = row['type']
		airrow[7] = 1
		airrow[8] = row.get('qar')
		airrow[10] = row['fdr']

		airrow[11] = row.get('cvr')
		airrow[32] = row['engine']		# Engine 1 type

		if recoders.has_key(row['fdr']):
			airrow[10] = recoders[row['fdr']]	# FDR
			# print row['fdr'], recoders[row['fdr']], airrow[10]
			# print airrow

		output.writerow(airrow)