import os, shutil, sys, string

# finds out what drive the flash drive is mounted to. 
 #list of all letters are other stuff at the end but mostly letters


def find_drive():
        drive = 'null'
        letter=''
        letternum=0
        allTheLetters = string.uppercase
        while letternum <26:
                letter =  allTheLetters[letternum:letternum+1]
                letternum +=1
                if os.path.exists( letter +':\ACDCallReportUpdate\QuickerCallReportupdate.py'):
                        drive = letter
                        break  
        return drive

def copy_and_overwrite(from_path, to_path): # used to make copies of the ACD reports from the thawed drive to the flash drive 
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def list_all_files(source):
    folders = os.listdir(source)
    directories = []
    for folder in folders:
        directories.append(source +"/"+ folder)
    return directories

def copy_new_files(source, dest):
    directories = list_all_files(source)
    #print directories
    for directory in directories:
        files = os.listdir(directory)
        #print "where is.."+ str(files)
        for text in files:
            full_file_name = os.path.join(directory, text)
            #print full_file_name
            finaldest = dest + directory[directory.find('/'): len(directory)]
            if (not os.path.exists(finaldest + "/" + text)):
                print "Got here"
                shutil.copy(full_file_name, finaldest)


drive = find_drive()
year = ""

BACKUP = "Z:ACD Reports\ACD Reports\ACD "

year = raw_input("What year do you want to copy? (Ex 2013, etc.)")

print "All new files for HELP, SFS, and ADMISS will be backed up to the network drive."

#copy_and_overwrite( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)
copy_new_files( drive+ ":\ACD Reports\ACD " + year, "Z:\ACD Reports\ACD Reports\ACD " +year)

