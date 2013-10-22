import os, shutil, sys, string
# finds out what drive the flash drive is mounted to. 
drive = 'null'
letter=''
letternum=0
allTheLetters = string.uppercase #list of all letters are other stuff at the end but mostly letters



def copy_and_overwrite(from_path, to_path): # used to make copies of the ACD reports from the thawed drive to the flash drive 
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def copy_new_files(filelist, dest):
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

while letternum <26:
    letter =  allTheLetters[letternum:letternum+1]
    letternum +=1
    if os.path.exists( letter +':\ACDCallReportUpdate\QuickerCallReportupdate.py'):
        drive = letter
        break  
#
SOURCE1 = drive +':\ACDCallReportUpdate\READMEforQuickerReportsUpdate.txt'
SOURCE2 = drive +':\ACDCallReportUpdate\QuickerCallReportupdate.py'
BACKUP = 'C:/Users/rebecca.murphy2/Documents/GitHub/ACDReportupdater'

shutil.copy(SOURCE1, BACKUP)
shutil.copy(SOURCE2, BACKUP)

copy_and_overwrite(drive+ ":/ACD 2013", "Z:ACD Reports\ACD Reports\ACD 2013")
