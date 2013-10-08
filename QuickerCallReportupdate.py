import os
import csv
import shutil
import string 

#All the starting data stuff
i = input('Enter Start Day: ')
l = i #l is the dummy day basically
m = raw_input('Enter Start Month (Full name or  number): ')
year = raw_input('Enter Year (2013,2014,etc): ')
months = ['january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december']

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

if isint(m):# used to tell is someone used a number for a month or a name
    startmonth = int(m)-1
else:
    startmonth = months.index(m.lower())

# finds out what drive the flash drive is mounted to. 
drive = 'null'
letter=''
letternum=0
allTheLetters = string.uppercase #list of all letters are other stuff at the end but mostly letters

while letternum <26:
    letter =  allTheLetters[letternum:letternum+1]
    letternum +=1
    if os.path.exists( letter +':\ACDCallReportUpdate\QuickerCallReportupdate.py'):
        drive = letter
        break  
#

answer = raw_input ("Do you want to copy ACD Reports? (y/n)")
if answer.lower() == 'y':
    SOURCE = "D:\ACD Reports\ACD " + year

    if os.path.exists(drive + ":\ACD " + str (int(year) -1)  ):
        answer = raw_input ("Starting a new year will delete all records last year from the flash drive. Do you want the records deleted? (y/n)")
        if answer.lower() == 'y':
            shutil.rmtree(drive + ":\ACD " + str (int(year) -1))
    else:
        print "The records were not deleted. Please note how much space is available on the flash drive."
    BACKUP = drive + ":\ACD " + year  
# create a backup directory
    print "Copying...Please Wait"
    copy_and_overwrite(SOURCE, BACKUP)

    print "Done Copying ACD Reports for " +year
    





dummymonth = startmonth
admissrecords = []
helprecords = []
sfsrecords = []
count =0 # used to see how much the loop has done, incase it wants to break after only going one month

while dummymonth < len(months): # goes through each department and saves teh records in an array. Coudl probably make more effecient, a function call prob instead of hard coding it 3 times
        month = months[dummymonth] 
        while l < 32:
                count+=1              
                if os.path.exists(letter +':\ACD '+ year +'\Admiss '+year+ '\Admiss ' + month +" " + str(l) + '.txt'):
                    openfile = open(letter+':\ACD '+ year +'\Admiss '+year+'\Admiss '+month +" " + str(l) + '.txt', 'r')
                    text = openfile.read()
                    
                    #hundreds 8 spaces
                    space1 = text.find("ADMISS      ") + len("ADMISS      ") 
                    space2 = text.find(" ", space1)
                    callnum = text[space1:space2]
                       
                    if len(callnum) != 3:  #tenths 9 spaces
                        space1 = text.find("ADMISS       ") + len("ADMISS       ")
                        space2 = text.find(" ", space1)
                        callnum = text[space1:space2]

                    if len(callnum) != 2 and len(callnum) !=3:
                        #singles 10
                        space1 = text.find("ADMISS        ") + len("ADMISS        ")  
                        space2 = text.find(" ", space1)
                        callnum = text[space1:space2]
                        
                    if callnum == 0 or not callnum: 
                        l+=1
                    else:
                        admissrecords.append([str(l)+'-'+month[0:3]+'-' +year[2:4],callnum])
                        l+=1
                else:
                    l+=1
        dummymonth+=1
        l=1
dummymonth=startmonth
l=i 
while dummymonth < len(months):
        month = months[dummymonth] 
        while l < 32:
                if os.path.exists(drive +':\ACD '+ year +'\Help '+year+'\Help ' + month +" " + str(l) + '.txt'):
                        openfile = open(drive+':\ACD '+ year +'\Help '+year+'\Help '+month +" " + str(l) + '.txt', 'r')
                        text = openfile.read()
                        
                        #hundreds 8 spaces 
                        space1 = text.find("HELP        ") + len("HELP        ") 
                        space2 = text.find(" ", space1)
                        callnum = text[space1:space2]
                       
                        if len(callnum) != 3:  #tenths 9 spaces
                                space1 = text.find("HELP         ") + len("HELP         ")
                                space2 = text.find(" ", space1)
                                callnum = text[space1:space2]

                        if len(callnum) != 2 and len(callnum) !=3:
                                #singles 10
                                space1 = text.find("HELP          ") + len("HELP          ")  
                                space2 = text.find(" ", space1)
                                callnum = text[space1:space2]
                        
                        if callnum == 0 or not callnum: 
                                l+=1
                        else:
                                helprecords.append([str(l)+'-'+month[0:3]+'-' +year[2:4], callnum])
                                l+=1
                        
                else:
                        l+=1
        dummymonth+=1
        l=1
dummymonth=startmonth
l=i
while dummymonth < len(months):
        month = months[dummymonth] 
        while l < 32:
                if os.path.exists(drive+':\ACD '+ year +'\SFS '+year+'\SFS ' + month +" " + str(l) + '.txt'):
                        openfile = open(drive+':\ACD '+ year +'\SFS '+year+'\SFS '+month +" " + str(l) + '.txt', 'r')
                        text = openfile.read()
                        
                        #hundreds 8 spaces 
                        space1 = text.find("SFS         ") + len("SFS         ") 
                        space2 = text.find(" ", space1)
                        callnum = text[space1:space2]
                       
                        if len(callnum) != 3:  #tenths 9 spaces
                                space1 = text.find("SFS          ") + len("SFS          ")
                                space2 = text.find(" ", space1)
                                callnum = text[space1:space2]

                        if len(callnum) != 2 and len(callnum) !=3:
                                #singles 10
                                space1 = text.find("SFS           ") + len("SFS           ")  
                                space2 = text.find(" ", space1)
                                callnum = text[space1:space2]
                         
                        if callnum == 0 or not callnum: 
                                l+=1
                        else:
                                sfsrecords.append([str(l)+'-'+month[0:3]+'-' +year[2:4],callnum])
                                l +=1
                        
                else:
                        l+=1
        dummymonth+=1
        l=1

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

print "Exported records to CSVs"
