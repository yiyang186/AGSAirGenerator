# -*- coding:utf8 -*-  

import xlrd, os, csv, sys
reload(sys)
sys.setdefaultencoding("utf-8")

crash, maint, frame = {}, {}, {}
dicts = {3:crash, 4:crash, 5:maint, 6:frame}

files = os.listdir('..'+os.sep+'input')
for filename in files:
	filedata = {}	# all data in the file
	workbook = xlrd.open_workbook('..'+os.sep+'input'+os.sep+filename)
	for booksheet in workbook.sheets():
		for row in range(1, booksheet.nrows):
			for col in range(3, booksheet.ncols):
				colvalue = str(booksheet.cell(row, col).value).replace('\n', '')
				colvalue = colvalue.replace('\r', '').strip()

				if col < 7 and not dicts[col].has_key(colvalue):
					dicts[col][colvalue] = filename

outputfile = ['crash', 'maint', 'frame']
for fstr in outputfile:
	f = open('..'+os.sep+'00000000'+fstr+'.csv', 'w')
	writer = csv.writer(f, delimiter=',')
	exec("for s in "+fstr+'.viewitems():writer.writerow(s)')
	f.close()