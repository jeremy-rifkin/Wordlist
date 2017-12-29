'''''''''''''''''''''''''''''''''''''''
''  Copyright (c) FelisPhasma 2015   ''
'''''''''''''''''''''''''''''''''''''''
import time
import os
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()
sourcePath = "res/"
sourceFiles = ['a.txt', 'c.txt', 'd.txt', 'e.txt']
#'b.txt',
# B excluded because of ascii control characters
def end():
	execTime = current_milli_time() - start
	print "Execution time: ", str(current_milli_time() - start), "ms"
	print "Execution time: ", str((current_milli_time() - start) / 1000), "sec"
	print "Execution time: ", str((current_milli_time() - start) / (60 * 1000)), "min"
	print "Execution time: ", str(((current_milli_time() - start) / (60 * 1000)) / 60), "hr"
def init():
	print("Init")
	tList = set()
	for fname in sourceFiles:
		with open(sourcePath + fname, "r") as infile:
			for line in infile:
				tList.add(line.lower().capitalize())
	print("Words compiled")
	dList = set()
	for i in tList:
		if i not in dList:
			dList.add(i)
	tList = None
	print("Duplicates removed")
	output = sorted(dList)
	dList = None
	outputFile = open("master.txt", "w+")
	for line in output:
		outputFile.write(line)
	end()
	print("Done")
init()
