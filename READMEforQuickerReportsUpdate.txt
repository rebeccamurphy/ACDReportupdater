Instructions:

Run the file on the computer wear CBX is always open. It will copy all the records of the current year to the flash drive as well as updating the csv. It should take a couple minutes for teh files to copy, so don't freak out. 

Double Click the .py file. 
Enter the start day to the updated records
Enter the month
Enter the year

While the script runs, it updates help.csv (for helpdesk), missions.csv (for admissions) and sfs.csv (for sfs)
when it's done, open one of the cvs and you can easily copy and past its contents into the right place on the Acd report Charts.xlsx on the network drive

Possible Errors:

if you see a bunch of #### it usually just means the excel collumn is not wide enough to show all the numbers. 

if the call collumn does not have a number, it means that there was not calls recieved recorded for that day, but feel free to actually check the text
file. 

Updates:

10/8/13
	Now it copies the ACD directory on the CBX computer, as well as exporting the data to the csvs. It takes a few minutes to copy all the data, so theres prob a more effecient way to copy everything.

Needed Updates:

Only copy new files, not all files from records.

Figure out what would happen when a new year starts. could probably keep it the way it is, and have to run it 2 different times from december 2013 and january 2014. 

Still appends 0 records sometimes. need to fix that. 