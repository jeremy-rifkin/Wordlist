import time
import os
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()
sourcePath = "res/"
sourceFiles = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
def compileWords():
    with open('tmp.txt', 'w') as outfile:
        for fname in sourceFiles:
            with open(sourcePath + fname, "r") as infile:
                for line in infile:
                    outfile.write(line)
def reSort():
    outputFile = open("master.txt", "w+")
    with open('tmp.txt', 'r') as r:
        for line in sorted(r):
            outputFile.write(line.capitalize())
    os.remove("tmp.txt")
def removeDuplicates():
    lines = open('master.txt', 'r').readlines()
    lines_set = set(lines)
    out = open('master.txt', 'w')
    for line in lines_set:
        out.write(line)
def end():
    execTime = current_milli_time() - start
    print "Execution time:", str(current_milli_time() - start), "ms"
    print "Execution time:", str((current_milli_time() - start) / 1000), "sec"
    print "Execution time:", str((current_milli_time() - start) / (60 * 1000)), "min"
    print "Execution time:", str(((current_milli_time() - start) / (60 * 1000)) / 60), "hr"

def initSequence():
    print "Init"
    compileWords()
    print "Compiled"
    removeDuplicates()
    print "Duplicates removed"
    reSort()
    print "Sorted"
    end()
initSequence()