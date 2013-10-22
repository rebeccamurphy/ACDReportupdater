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

def copy_new_files(scr_files, dest):
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

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

def data_crawl(dept, records, startday):
    l = startday
    dummymonth = startmonth
    #count =0
    while dummymonth < len(months): # goes through each department and saves the records in an array. Could probably make more effecient, a function call prob instead of hard coding it 3 times
            month = months[dummymonth] 
            while l < 32:
                    #count+=1              
                    if os.path.exists(drive +':/ACD Reports/ACD '+ year +'/'+ dept +' '+year+'/'+ dept +' '+ month +" " + str(l) + '.txt'):
                        openfile = open(drive+':/ACD Reports/ACD'+ year +'/' +dept +' ' +year+'/'+ dept+ ' '+month +" " + str(l) + '.txt', 'r')
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