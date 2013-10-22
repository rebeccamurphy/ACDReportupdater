import os, shutil, sys, string, functions

# finds out what drive the flash drive is mounted to. 
 #list of all letters are other stuff at the end but mostly letters



drive = functions.find_drive()
year = ""

BACKUP = "Z:ACD Reports\ACD Reports\ACD "

year = raw_input("What year do you want to copy? (Ex 2013, etc.)")

print "All new files for HELP, SFS, and ADMISS will be backed up to the network drive."

#copy_and_overwrite( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)
functions.copy_new_files( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)

