#Youtube transcripts to text converter application - free 
#
#This python script removes the numbers from the transcript that one gets from youtube
#
#Step 1: download the file
#Step 2: place the file in the same folder as this python script
#Step 3: Run this python script in the terminal or just click on the file.
#Step 4: Enter the name of the file you need to modify WITH the EXTENSION
#Step 5: A file by the same name with sufix Filtered will be generated
#
# Author - SKRelan 
# www.github.com/skrelan

import re 	#Regular Expression module

def removeNumbers(fileName):
	fhand = open(fileName+'.txt','r')
	fwrite = open(fileName+'Filterd.txt','w')
	counter = 0
	space = 5  #This number decides how often a new line is written into the file 						
	for line in fhand:
		counter = counter + 1
		writes = re.findall('[^0-9:]',line)
		writes = ''.join(writes)
		#print writes
		fwrite.write(writes)
		if counter%space==0 :       
			fwrite.write('\n')
	fhand.close()
	fwrite.close()

# The main code	
fName = raw_input('Enter the file name with EXTENSION: ')
removeNumbers(fName[0:fName.find('.')])

# Author - SKRelan 
# www.github.com/skrelan