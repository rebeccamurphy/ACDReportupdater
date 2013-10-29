import os, csv,shutil,string, functions
months = ['jan', 'feb','mar','apr','may', 'jun', 'jul', 'aug','sep','oct','nov','dec']
#All the starting data stuff

print "Getting Day last updated..."
drive = functions.find_drive()

lastdayup2= open(drive+':\ACDCallReportUpdate\lastdayupdated.txt', 'r' )
date= lastdayup2.readline()
index1 =date.find('-')
i = int(date[0:index1])
index2 = date.find('-', index1+1)
m = date[index1+1:index2]
startmonth = months.index(m.lower()[0:3])
year = "20" + date[index2+1:len(date)]
lastdayup2.close()

l = i #l is the dummy day basically
# Testing stuff so you dont ave to wait for it to copy if you dont want. 

SOURCE =  "D:\ACD Reports\ACD " + year
BACKUP = drive + ":\ACD Reports\ACD " + year  
if (os.path.exists(SOURCE)):
    print "Copying ACD Reports...Please Wait"
    if not (os.path.exists(drive + ":\ACD " + year)):
        functions.copy_and_overwrite(SOURCE, BACKUP)
    else: 
        functions.copy_new_files(SOURCE,BACKUP)
    print "Done Copying ACD Reports for " +year
    print "Starting to read through the records..."

admissrecords = []
helprecords = []
sfsrecords = []

admissdate =''
helpdate =''
sfsdate =''

def data_crawl(dept, records, startday, lastdayupdated):
    lastdayupdated =''
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
                            
                        if callnum == '0'or callnum == 0 or not callnum: #still can let a zero get appended. annoying.
                            l+=1
                        else:
                            records.append([str(l)+'-'+month[0:3]+'-' +year[2:4],callnum])
                            lastdayupdated = str(l)+'-'+month[0:3]+'-' +year[2:4]
                            l+=1
                    else:
                        l+=1
            dummymonth+=1
            l=1
    dummymonth=startmonth
    l=i
 

data_crawl('Admiss', admissrecords, l, admissdate)
data_crawl('Help', helprecords, l, helpdate )
data_crawl('Sfs', sfsrecords, l, sfsdate)

#print lastdayup.readline();
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
