#!/usr/bin/env python2.7
################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 5-3-2019
# Github Repo: https://github.com/cyberstorm-team-5/P7-Steg-Team-Chinese
# Description: Program 7: Steg
#              The Python code will implement both the bit and byte steg
#              algorithms for storing and retrieving data. The sentiel value
#              will be six bytes appended left to right to the hidden data. 
################################################################################

import sys

################################################################################

#global vars here
DEBUG = True

#general usage message
GENERAL_USAGE = "General Usage: ./steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]"
STORAGE_USAGE = "Store Data Usage: ./steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> -h<val>"

#sentinel value for keeping track of where the data ends
SENTINEL = chr(0) + chr(255) + chr(0) + chr(0) + chr(255) + chr(0)

################################################################################

#process the storage (hiding) of data into a wrapper file
def storeData(wrapper, offset):

	#retrieve file to hide inside of wrapper
	hidden = getHidden()
	
	#use byte or bit method based on args, otherwise specify usage
	if(sys.argv[1] == "-B"):
		#byte method
		i = 0
		#while (i < len(hidden)):
			#wrapper[


	elif(sys.argv[1] == "-b"):
		pass

	#inform user of proper way to use command line arguments
	else:
		print(STORAGE_USAGE)
		exit()



#process the retrieval of data from 
def retrieveData(wrapper, offset):
	
	#use byte or bit method based on args, otherwise specify usage
	if(sys.argv[1] == "-B"):
		#byte method
                interval = getInterval()
                
		hiddenData = ""
		#############NOTE: THIS IS NOT YET WORKING, CANNOT PROCESS SENTINEL PROPERLY
		while (hiddenData[-6:] != SENTINEL):
			#hiddenData += (chr(0) + chr(255) + chr(0) + chr(0) + chr(255) + chr(0))
                        hiddenData += ((wrapper[offset]))
                        offset += interval
                        print(hiddenData[-6:] + "\n")
                        

                        
		print(hiddenData)

	elif(sys.argv[1] == "-b"):
		#bit method
		pass

	#inform user of proper way to use command line arguments
	else:
		print(GENERAL_USAGE)
		exit()



#retrieve file to hide inside of wrapper from current directory based on command line arg
def getHidden():
	
	if(sys.argv[-1][:2] == "-h"):
		return open(sys.argv[-1][2:], 'rb').read()

	#inform user that hidden file is required for storage mode
	else:
		print(STORAGE_USAGE)
		exit()



#ensure a wrapper file was provided in command line arg from current directory and open it
def getWrapper():
	
	if(sys.argv[-1][:2] == "-w"):
		return open(sys.argv[-1][2:], 'rb').read()

	elif(sys.argv[-2][:2] == "-w"):
		return open(sys.argv[-2][2:], 'rb').read()

	#inform user of proper usage and exit
	else:
		print(GENERAL_USAGE)
		exit()


#ensure interval was specified and return its value if so
def getInterval():

        #return the interval if found
        if(sys.argv[4][:2] == "-i"):
            return int(sys.argv[4][2:])

        #inform user of proper usage and exit
        else:
            print(GENERAL_USAGE)
            exit()

#ensure an offset was specified and return its value if so
def getOffset():

	#return the offset if found
	if(sys.argv[3][:2] == "-o"):
		return int(sys.argv[3][2:])
	
	#inform user of proper usage and exit
	else:
		print(GENERAL_USAGE)
		exit()



###############################MAIN#############################################

#read in arguments from the command line, specifying proper usage if necessary
if(len(sys.argv) < 5):
	print(USAGE)

#ensure wrapper file provided (needed regardless of method used)
wrapper = getWrapper()

#ensure offset specified
offset = getOffset()


#go to the appropriate function to store (hide) data or retrieve it
if(sys.argv[2] == "-s"):
	storeData(wrapper, offset)

elif(sys.argv[2] == "-r"):
	retrieveData(wrapper, offset)

#invalid mode specified
else:
	print(GENERAL_USAGE)



