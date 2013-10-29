import os, shutil, sys, string, functions

# finds out what drive the flash drive is mounted to. 
 #list of all letters are other stuff at the end but mostly letters



drive = functions.find_drive()
year = ""

lastdayup2= open(drive+':\ACDCallReportUpdate\lastdayupdated.txt', 'r' )
date= lastdayup2.readline()
index1 =date.find('-')
index2 = date.find('-', index1+1)
year = "20" + date[index2+1:len(date)]
lastdayup2.close()

BACKUP = "Z:ACD Reports\ACD Reports\ACD "


print "All new files for PreHELP, HELP, PreSFS, SFS, and ADMISS will be backed up to the network drive. \n"
print "Copying...Please Wait..."
#copy_and_overwrite( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)

if os.path.exists("Z:\ACD Reports\ACD Reports\ACD " +year):
    functions.copy_new_files( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)
else: 
    functions.copy_and_overwrite( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)
print "Done"