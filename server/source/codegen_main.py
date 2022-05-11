#!/usr/bin/env python
# coding=utf-8
import os, sys
import codegen_xml_reader
import codegen_generator_ros
import codegen_generator_opcua

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
# Author: SRFG, Mathias Schmoigl-Tonis
# Project: ROBxTASK
# Date: Q1-Q2 2022
#--------------------------------------------
if __name__== "__main__":

	# check for correct program inputs via command line
	# only valid call if args = [strInputFile][strOutputFile][bSimulEnv]
	# sample call e.g. "python codegen_main.py ../input/example_2.xml ../output/generated_results/ false"
	print ("-----------------------------------------------------")
	print ('Codegen started with argument List:\n', str(sys.argv))
	print ("-----------------------------------------------------")

	if len(sys.argv) != 4:
		print('Codegen called with incorrect number of program arguments.')
		print('Try use the following syntax: python codegen_main.py [strInputFile][strOutputFile][bSimulEnv]')
		print('Program execution will stop now...')
		sys.exit()
	
	# trying to parser read blocks from XML project file
	# will create a list of blocks for every detected asset (SetAsset)
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]
	bIsSimulEnv = sys.argv[3].lower()

	if not os.access(inputFileName, os.R_OK): # check if inputFile is readable by system
		print('Codegen called with incorrect program argument. [strInputFile] is not readable!')
		print('Program execution will stop now...')
		sys.exit()
	#if not os.access(outputFileName, os.W_OK): # check if outputFile is writable by system	
	#	print('Codegen called with incorrect program argument. [strOutputFile] is not writable!')
	#	print('Program execution will stop now...')
	#	sys.exit()

	xml_parser = codegen_xml_reader.XML_BlocklyProject_Parser(inputFileName)
	xml_parser.readAssets()
	
	# check if real robot mode or simulated OPCUA mode
	# creates either ROS action clients for every found asset OR
	# creates OPCUA agent for every found asset
	if bIsSimulEnv == 'false':
		ros_gen = codegen_generator_ros.ROSGeneratorClass('_client_py', xml_parser.getList())
		ros_gen.dump_all(outputFileName)
		print ("-----------------------------------------------------")
		print ("Generation of ROS action client files succesfull!")
		print ("-----------------------------------------------------")
	elif bIsSimulEnv == 'true':
		ros_gen = codegen_generator_opcua.OPCUAGeneratorClass('_client_py', xml_parser.getList())
		ros_gen.dump_all(outputFileName)
		print ("-----------------------------------------------------")
		print ("Generation of OPCUA agent files succesfull!")
		print ("-----------------------------------------------------")
	else:
		print('Codegen called with incorrect program argument. [bSimulEnv] is not a boolean!')
		print('Program execution will stop now...')
		sys.exit()

	