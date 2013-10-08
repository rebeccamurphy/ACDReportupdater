import os
import csv
import shutil 

i = input('Enter Start Day: ')
l = i
m = raw_input('Enter Start Month: ')
year = raw_input('Enter Year (2013,2014,etc): ')
months = ['january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december']
startmonth = months.index(m.lower())
dummymonth = startmonth
admissrecords = []
helprecords = []
sfsrecords = []
count =0
#for l ln days:
while dummymonth < len(months):
        month = months[dummymonth] 
        l = i
        while l < 32:
                count+=1
                if os.path.exists('I:\ACD\Admiss '+year+ '\Admiss ' + month +" " + str(l) + '.txt'):
                        openfile = open('I:\ACD\Admiss '+year+'\Admiss '+month +" " + str(l) + '.txt', 'r')
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
                                drive = 'I'
                                l+=1
                        
                elif os.path.exists('E:\ACD\Admiss '+year+'\Admiss ' + month +" " + str(l) + '.txt'):
                        openfile = open('E:\ACD\Admiss '+year+'\Admiss '+month +" " + str(l) + '.txt', 'r')
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
                                drive = 'E'

                elif os.path.exists('F:\ACD\Admiss '+year+'\Admiss ' + month +" " + str(l) + '.txt'):
                        openfile = open('F:\ACD\Admiss '+year+'\Admiss '+month +" " + str(l) + '.txt', 'r')
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
                                drive = 'F'
								
                elif os.path.exists('G:\ACD\Admiss '+year+'\Admiss ' + month +" " + str(l) + '.txt'):
                        openfile = open('G:\ACD\Admiss '+year+'\Admiss '+month +" " + str(l) + '.txt', 'r')
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
                                drive = 'G'
                                
                                                
                elif count==1 and l==31:
                        l=1
                        month=months[dummymonth+1]
                else:
                        l+=1
                        
        dummymonth+=1
dummymonth=startmonth
while dummymonth < len(months):
        l = i
        month = months[dummymonth] 
        while l < 32:
                if os.path.exists(drive +':\ACD\Help '+year+'\Help ' + month +" " + str(l) + '.txt'):
                        openfile = open(drive+':\ACD\Help '+year+'\Help '+month +" " + str(l) + '.txt', 'r')
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

dummymonth=startmonth
while dummymonth < len(months):
        l = i
        month = months[dummymonth] 
        while l < 32:
                if os.path.exists(drive+':\ACD\SFS '+year+'\SFS ' + month +" " + str(l) + '.txt'):
                        openfile = open(drive+':\ACD\SFS '+year+'\SFS '+month +" " + str(l) + '.txt', 'r')
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
