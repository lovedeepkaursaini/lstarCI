#!usr/bin/python

import os


def generateFileName(begin, numEvts):
    end = begin+numEvts
    return "fstar_"+str(begin)+"_"+str(end)+".lhe"

def runSplitEngine(begin, numEvts):
    cmd = "./splitLheFile fstar.lhe"
    cmd = cmd +" "+str(begin)+" "+str(numEvts)
    cmd = cmd +" "+generateFileName(begin,numEvts)
    os.system(cmd)
 

def Main():
    outFile = "fstar"
    evtPerFile = 10
    cumEvts = 0;
    for i in range(0,1000):
        runSplitEngine(cumEvts,evtPerFile)
        cumEvts +=evtPerFile
        

Main()
