import os, shutil, sys, string
# finds out what drive the flash drive is mounted to. 
drive = 'null'
letter=''
letternum=0
allTheLetters = string.uppercase #list of all letters are other stuff at the end but mostly letters


drive = find_drive()
#
SOURCE1 = drive +':\ACDCallReportUpdate\READMEforQuickerReportsUpdate.txt'
SOURCE2 = drive +':\ACDCallReportUpdate\QuickerCallReportupdate.py'
BACKUP = 'C:/Users/rebecca.murphy2/Documents/GitHub/ACDReportupdater'

#shutil.copy(SOURCE1, BACKUP)
#shutil.copy(SOURCE2, BACKUP)

#copy_and_overwrite(drive+ ":/ACD 2013", "Z:ACD Reports\ACD Reports\ACD 2013")
functions.copy_new_files1(drive+ ":\ACDCallReportUpdate", "C:/Users/rebecca.murphy2/Documents/GitHub/ACDReportupdater")