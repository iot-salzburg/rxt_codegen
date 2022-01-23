#!/usr/bin/env python
# coding=utf-8
import sys
import codegen_xml_reader
import codegen_ros_generator
import codegen_opcua_generator

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
if __name__== "__main__":

	# check for correct program inputs via command line
	print ('Codegen started with number of arguments:', len(sys.argv), 'arguments.')
	print ('Codegen started with argument List:', str(sys.argv))

	if len(sys.argv) != 4:
		print('Codegen called with incorrect number of program arguments.')
		print('Try use the following syntax: python codegen_main.py [strInputFile][strOutputFile][bSimulEnv]')
		print('Program execution will stop now...')
		sys.exit()
	
	print ("Trying to parse XML input file now...")
	inputFileName = sys.argv[1] # e.g. '../input/example_oliver.xml'
	outputFileName = sys.argv[2] # e.g. '../output/auto_generated.py'
	bIsSimulEnv = sys.argv[3].lower() # true OR false
	
	# parser read blocks from XML
	xml_parser = codegen_xml_reader.XML_BlocklyProject_Parser(inputFileName)
	xml_parser.readAssets()
	listBlocks = xml_parser.readBlocks()
	
	# check if real robot mode or simulated OPCUA mode
	if bIsSimulEnv == 'false':
		ros_gen = codegen_ros_generator.ROSGeneratorClass('qbo_client_py', listBlocks)
		ros_gen.dump_self(outputFileName)
	else:
		ros_gen = codegen_opcua_generator.OPCUAGeneratorClass('qbo_client_py', listBlocks)
		ros_gen.dump_self(outputFileName)

