# Auto generated configuration file
# using: 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

################################################################################
# Basic running parameters (modify to your needs)
index=1

#   random seed
theSeedValue = int(9583985+1000*index)
print 'Seed value: '+str(theSeedValue)

################################################################################


# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring( "file:fstar.lhe"),
    firstRun = cms.untracked.uint32( index  )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/FourteenTeV/Hadronizer_TuneZ2star_14TeV_madgraph_tauola_cff.py nevts:10000'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string("fstar_GEN.root"),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All','')#MCRUN2_71_V1::All', '')

process.load('IOMC/RandomEngine/IOMC_cff')
process.RandomNumberGeneratorService.generator.initialSeed  = theSeedValue+111 ###cms.untracked.uint32(1136201) #########
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = theSeedValue+222 ###cms.untracked.uint32(2132001)
process.RandomNumberGeneratorService.g4SimHits.initialSeed  = theSeedValue+333 ###cms.untracked.uint32(3136201)


# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)


