import os, csv,shutil,string, functions

#All the starting data stuff
i = input('Enter Start Day: ')
l = i #l is the dummy day basically
m = raw_input('Enter Start Month (Full name or number): ')
year = raw_input('Enter Year (2013,2014,etc): ')
months = ['january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december']


if isint(m):# used to tell is someone used a number for a month or a name make into a function 
    startmonth = int(m)-1
else:
    startmonth = months.index(m.lower())

# finds out what drive the flash drive is mounted to. 
drive = 'null'
letter=''
letternum=0
allTheLetters = string.uppercase #list of all letters are other stuff at the end but mostly letters

drive = functinos. find_drive()
#

# Testing stuff so you dont ave to wait for it to copy if you dont want. 
answer = raw_input ("Do you want to copy ACD Reports? (y/n)")
if answer.lower() == 'y':
    SOURCE =  "D:\ACD Reports\ACD " + year
    src_files1 = os.listdir(SOURCE + "\Admiss 2013")
    src_files2 = os.listdir(SOURCE + "\Help 2013")
    src_files3 = os.listdir(SOURCE + "\SFS 2013")

    if os.path.exists(drive + ":\ACD " + str (int(year) -1)  ):
        answer = raw_input ("Starting a new year will delete all records last year from the flash drive. Do you want the records deleted? (y/n)")
        if answer.lower() == 'y':
            shutil.rmtree(drive + ":\ACD " + str (int(year) -1))
        else:
            print "The records were not deleted. Please note how much space is available on the flash drive."
    BACKUP = drive + ":\ACD Reports\ACD " + year  

    answer = raw_input("Enter 0: to only copy the new files. (much faster) \n" + "Enter 1: to copy and overwrite all files. (Takes longer, but useful if the other method doesn't work.)")
    # create a backup directory
    print "Copying...Please Wait"
    if (answer == 1)
        functions.copy_and_overwrite(SOURCE, BACKUP)
    if (answer == 0)
        functions.copy_new_files(SOURCE,BACKUP)
    print "Done Copying ACD Reports for " +year
    
#starts extracting the relevant records

print "Starting to read through the records..."


admissrecords = []
helprecords = []
sfsrecords = []



functions.data_crawl('Admiss', admissrecords, l)
functions.data_crawl('Help', helprecords, l)
functinos.data_crawl('Sfs', sfsrecords, l)


with  open(drive+':\ACDCallReportUpdate\missions.csv', 'wb') as admissfile:
        admisswriter = csv.writer(admissfile)
        for x in admissrecords:
                admisswriter.writerow(x)
                
with open(drive+':\ACDCallReportUpdate\help.csv', 'wb') as helpfile: 
        helpwriter = csv.writer(helpfile)
        for x in helprecords:
                helpwriter.writerow(x)
with open(drive+':\ACDCallReportUpdate\sfs.csv', 'wb') as sfsfile:
        sfswriter = csv.writer(sfsfile)
        for x in sfsrecords:
                sfswriter.writerow(x)


admissfile.close()
helpfile.close()
sfsfile.close()

print "Done"
