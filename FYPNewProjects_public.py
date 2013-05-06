#!/usr/bin/python
import sys
#===========================================================================
#The MAIN function
def startAnalysis():
    debug=0
    #if debug==1: startTime = time.time()
    inFile_FYPList = 'FYPOldList.txt'
    inFile_NewList = 'FYPNewList.txt'
    outFile_results = 'FYP_allNew.txt'
    oldList = {}
    newList = {}

    try:
        file_inFYPList = open(inFile_FYPList, 'r')
    except:
        print "\nUSER ERROR: There is no FYPOldList.txt - Please create a txt file and name it FYPOldList.txt"
        sys.exit(2)

    try:
        file_inNewList = open(inFile_NewList, 'r')
    except:
        print "\nUSER ERROR: There is no FYPNewList.txt - Please create a txt file and name it FYPNewList.txt"
        sys.exit(2)

    for eachLine in file_inFYPList:
        try:
            serialNum, projID, details = eachLine.split('\t', 2)
            oldList[projID] = details
        except ValueError: pass

    for eachLine in file_inNewList:
        try:
            serialNum, projID, details = eachLine.split('\t', 2)
            if projID not in oldList.keys():
                newList[int(serialNum)] = eachLine
        except ValueError: pass

    file_outResults = open(outFile_results, 'w')
    for eachSerialNum in sorted(newList.keys()):
        print newList[eachSerialNum]
        print >> file_outResults, newList[eachSerialNum]

#==================================================
def usage():
    print "usage: " + sys.argv[0] + "\n" + "Save the list you read previously under the file name FYPOldList.txt" \
    + "\n" + "Save the current list under the file name FYPNewList.txt" + "\n" + "The new results will appear in FYP_allNew.txt"
#==================================================
usage()
startAnalysis()








