import re, os

LIST = """
fstar_0_10.lhe
fstar_10_20.lhe
"""

#datasets =  LIST.split()

datasets = []
for i in range(475,1000):
   datasets.append("fstar_"+str(i*10)+"_"+str((i+1)*10)+".lhe")

#for file in datasets:
#   print file

   
def createCfg():
    sourceCfg = open("baseCrab.cfg","r")
    Lines = sourceCfg.readlines()
    sourceCfg.close()
    
    for dataset in datasets:
        dirName = dataset.split(".")[0]
        newCfg = open("%s.cfg"%dirName,"w")
        for line in Lines:
            if "output_file" in line:
                newCfg.write("output_file = out_%s.root\n"%dirName)
            elif "pset" in line:
                newCfg.write("pset=%s_lhetoRECO_cfg.py\n"%dirName)
            elif "additional_input_files" in line:
                newCfg.write("additional_input_files=%s.lhe\n"%dirName)
            elif "ui_working_dir" in line:
                newCfg.write("ui_working_dir=%s\n"%dirName)
            else:
                newCfg.write(line)
        newCfg.close()

def clean():
    for dataset in datasets:
        dirName = dataset.split(".")[0]
        com = "rm -rf %s"%dirName
        print com
        os.system(com)

def createJobs():
    for dataset in datasets:
        dirName = dataset.split(".")[0]
        com = "crab -cfg %s.cfg -create -submit"%dirName
        print com
        os.system(com)

def status():
    for dataset in datasets:
        dirName = dataset.split("/")[1]
        com = "crab -c %s -status -getoutput"%dirName
        print com

#clean()
createCfg()
createJobs()
#status()
