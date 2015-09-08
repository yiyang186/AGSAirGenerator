# -*- coding:utf8 -*-  

import os, csv, sys
import lib

reload(sys)
sys.setdefaultencoding("utf-8")

today = lib.others.gettoday()
recoders = lib.getindices.get_fdr_indices({})

# ouput .air file from ./input/*.xls or *.xlsx
output = csv.writer(file('..'+os.sep+'output.air', 'wb'), delimiter='\t')
head = '''// A/C tail	Reception date	Airline	A/C type	A/C type wired no	A/C ident	A/C serial number	A/C in operation (1=YES/0=NO)	Maintenance recorder model	Maintenance recorder 2 model	Crash recorder model	Crash recorder 2 model	Version for analysis/maintenance	Version for analysis/maintenance 2	Version for analysis/crash	Version for analysis/crash2	A/C maintenance link (A=By file (Aligned Bit), B=By file (Bitstream), D=Direct)	A/C maintenance 2 link	A/C crask link	A/C crash 2 link	Maintenance recorder serial number	Maintenance 2 recorder serial number	Crash recorder serial number	Crash recorder 2 serial number	Engine 1 serial number	Engine 2 serial number	Engine 3 serial number	Engine 3 serial number	Engine 1 installation date	Engine 2 installation date	Engine 3 installation date	Engine 4 installation date	Engine 1 type	Engine 2 type	Engine 3 type	Engine 4 type	Maintenance recorder maximum duration for discontinuity between 2 recordings	Maintenance recorder max duration since last recording	Maintenance recorder 2 maximum duration for discontinuity between 2 recordings	Maintenance recorder 2 max duration since last recording	Crash recorder maximum duration for discontinuity between 2 recordings	Crash recorder max duration since last recording	Crash recorder 2 maximum duration for discontinuity between 2 recordings	Crash recorder 2 max duration since last recording	(Spare)	(Spare)	(Spare)	(Spare)	Crash recorder automatic frame reorganization	Maintenance recorder automatic frame reorganization	Crash recorder 2 automatic frame reorganization	Maintenance recorder 2 automatic frame reorganization'''
output.writerow(head.split('\t'))
output.writerow(['//AGS'])
files = os.listdir('..'+os.sep+'input')
for filename in files:
	lib.convertor.convertfile(filename, output, recoders, today)