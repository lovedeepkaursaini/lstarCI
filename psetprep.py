import re, os

LIST = """
fstar_0_10.lhe
fstar_10_20.lhe
"""

datasets = []
for i in range(0,1000):
   datasets.append("fstar_"+str(i*10)+"_"+str((i+1)*10)+".lhe")

def createCfg():
    sourceCfg = open("lhetoRECO_cfg.py","r")
    Lines = sourceCfg.readlines()
    sourceCfg.close()
    
    for dataset in datasets:
        dirName = dataset.split(".")[0]
        print dirName
        newCfg = open("%s_lhetoRECO_cfg.py"%dirName,"w")
        for line in Lines:
            if "out_all.root" in line:
                newCfg.write("    fileName = cms.untracked.string('out_%s.root'),\n"%dirName)
            elif "    fileNames = cms.untracked.vstring( 'file:fstar.lhe')," in line:
                newCfg.write("    fileNames = cms.untracked.vstring( 'file:%s.lhe'),\n"%dirName)
            else:
                newCfg.write(line)
        newCfg.close()

createCfg()
