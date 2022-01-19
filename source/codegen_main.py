#!/usr/bin/env python
# coding=utf-8
import codegen_xml_reader
import codegen_python_generator

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
if __name__== "__main__":

	print ("Trying to parse XML input file now...")
	
	xml_parser = codegen_xml_reader.XML_BlocklyProject_Parser()
	xml_parser.readAssets()
	listBlocks = xml_parser.readBlocks()
	
	python_gen = codegen_python_generator.PythonGeneratorClass('qbo_client_py', listBlocks)
	python_gen.dump_self('../output/auto_generated.py')