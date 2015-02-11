# Auto generated configuration file
# using: 
# Revision: 1.353 
# Source: /local/reps/CMSSW.admin/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/MustarToMuG_L10000_M1000_8TeV_pythia8_cff.py --step GEN,SIM --beamspot Realistic8TeVCollision --conditions START50_V13::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.353 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/MustarToMuG_L10000_M1000_8TeV_pythia8_cff.py nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('MustarToMuG_8TeV_pythia8_cff_py_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START53_V27::All'

process.generator = cms.EDFilter("Pythia8175GeneratorFilter",
				 maxEventsToPrint = cms.untracked.int32(10),
				 pythiaPylistVerbosity = cms.untracked.int32(1),
				 pythiaHepMCVerbosity = cms.untracked.bool(False),
				 filterEfficiency = cms.untracked.double(1.),
				 comEnergy = cms.double(8000.0),
				 crossSection = cms.untracked.double(0.04833),
				 PythiaParameters = cms.PSet(
	processParameters = cms.vstring(
	'Tune:pp 5',
	'ExcitedFermion:qqbar2eStare = on',
	'ExcitedFermion:Lambda= 10000',
	'4000011:onMode = off',
	'4000011:onIfMatch = 11 23',
	'4000011:m0 = 1000',
	'23:onMode = off',
	'23:onIfMatch = 1 1',
	'23:onIfMatch = 2 2',
	'23:onIfMatch = 3 3',
	'23:onIfMatch = 4 4',
	'23:onIfMatch = 5 5'
	),
	parameterSets = cms.vstring('processParameters')
	))

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

