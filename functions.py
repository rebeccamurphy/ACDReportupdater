import os, shutil, sys, string
def isint(x): # used to tell is someone used a number for a month or a name
    try:
        a = int(x)
    except ValueError:
        return False
    else:
        return True 

def copy_and_overwrite(from_path, to_path): # used to make copies of the ACD reports from the thawed drive to the flash drive 
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

'''def copy_new_files(scr_files, dest):
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)
'''
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

def copy_new_files(source, dest): #has inner folders
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
                shutil.copy(full_file_name, finaldest)

def copy_new_files1(source, dest): # no inner folders
    directory = list_all_files(source)
    for text in directory:
        full_file_name = os.path.join(directory, text)
        shutil.copy(full_file_name, dest)

