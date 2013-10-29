import os, csv,shutil,string, functions

#All the starting data stuff
i = input('Enter Start Day: ')
l = i #l is the dummy day basically
m = raw_input('Enter Start Month (Full name or number): ')
year = raw_input('Enter Year (2013,2014,etc): ')
months = ['january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december']


if functions.isint(m):# used to tell is someone used a number for a month or a name make into a function 
    startmonth = int(m)-1
else:
    startmonth = months.index(m.lower())

drive = functions.find_drive()
# Testing stuff so you dont ave to wait for it to copy if you dont want. 
answer = raw_input ("Do you want to copy ACD Reports? (y/n)")
if answer.lower() == 'y':
    #SOURCE =  "Z:\ACD Reports\ACD Reports\ACD " + year
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

    answer = input("Enter 0: to only copy the new files. (much faster) \n" + "Enter 1: to copy and overwrite all files. (Takes longer, but useful if the other method doesn't work.)")
    # create a backup directory
    print "Copying...Please Wait"
    if (answer == 1):
        functions.copy_and_overwrite(SOURCE, BACKUP)
        
    if (answer == 0):
        functions.copy_new_files(SOURCE,BACKUP)
        print "got here"
    print "Done Copying ACD Reports for " +year
    
#starts extracting the relevant records

print "Starting to read through the records..."


admissrecords = []
helprecords = []
sfsrecords = []

def data_crawl(dept, records, startday):
    months = ['january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december']
    l = startday
    dummymonth = startmonth
    #count =0
    while dummymonth < len(months): # goes through each department and saves the records in an array. Could probably make more effecient, a function call prob instead of hard coding it 3 times
            month = months[dummymonth] 
            while l < 32:
                    #count+=1              
                    if os.path.exists(drive +':/ACD Reports/ACD '+ year +'/'+ dept +' '+year+'/'+ dept +' '+ month +" " + str(l) + '.txt'):
                        openfile = open(drive+':/ACD Reports/ACD '+ year +'/' +dept +' ' +year+'/'+ dept+ ' '+month +" " + str(l) + '.txt', 'r')
                        text = openfile.read()
                        
                        #hundreds 12 chars total
                        hundredspace = " " * (12-len(dept))

                        space1 = text.find (dept.upper() + hundredspace) + len(dept.upper()+ hundredspace) 
                        space2 = text.find(" ", space1)
                        callnum = text[space1:space2]
                           
                        if len(callnum) != 3:  #tenths 13 chars total
                            tenthsspace = " " * (13-len(dept))
                            space1 = text.find(dept.upper()+ tenthsspace) + len(dept.upper()+tenthsspace)
                            space2 = text.find(" ", space1)
                            callnum = text[space1:space2]

                        if len(callnum) != 2 and len(callnum) !=3:
                            #singles 14 char total 
                            singlespace = " " * (14-len(dept))
                            space1 = text.find(dept.upper()+singlespace) + len(dept.upper()+singlespace)  
                            space2 = text.find(" ", space1)
                            callnum = text[space1:space2]
                            
                        if callnum == 0 or not callnum: #still can let a zero get appended. annoying.
                            l+=1
                        else:
                            records.append([str(l)+'-'+month[0:3]+'-' +year[2:4],callnum])
                            l+=1
                    else:
                        l+=1
            dummymonth+=1
            l=1
    dummymonth=startmonth
    l=i

data_crawl('Admiss', admissrecords, l)
data_crawl('Help', helprecords, l )
data_crawl('Sfs', sfsrecords, l)


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
