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

def getlastupdated(date, i, m, year):
    index1 =date.find('-')
    i = int(date[0:index1])
    index2 = date.find('-', index1+1)
    m = date[index1+1:index2]
    startmonth = months.index(m.lower()[0:3])
    year = "20" + date[index2+1:len(date)]

def getmostcurrentday(date1, date2, date3, lastdayupdated):
    
    index1 =date1.find('-')
    i1 = int(date1[0:index1])
    index2 = date1.find('-', index1+1)
    m1 = date1[index1+1:index2]
    year1 = "20" + date1[index2+1:len(date1)]

    index1 =date2.find('-')
    i2 = int(date2[0:index1])
    index2 = date2.find('-', index1+1)
    m2 = date2[index1+1:index2]
    year2 = "20" + date2[index2+1:len(date2)]

    index1 =date3.find('-')
    i3 = int(date3[0:index1])
    index3 = date3.find('-', index1+1)
    m3 = date3[index1+1:index2]
    year3 = "20" + date3[index2+1:len(date3)]

    year = max( [year1, year2, year3 ])



def writelastupdate(lastdayupdated):
    if lastdayupdated != '':
        lastdayup2= open(drive+':\ACDCallReportUpdate\lastdayupdated.txt', 'w' )
        lastdayup2.write(lastdayupdated)
        lastdayup2.close()