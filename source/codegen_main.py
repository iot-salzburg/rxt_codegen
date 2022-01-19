#!/usr/bin/env python
# coding=utf-8
import codegen_xml_reader
import codegen_python_generator

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
if __name__== "__main__":

	print ("Trying to parse XML input file now...")
	
	codegen_xml_reader.readAssets()
	listBlocks = codegen_xml_reader.readBlocks()
	
	p = codegen_python_generator.GeneratorClass_StaticContent('qbo_client_py', listBlocks)
	p.dump_self('../output/auto_generated.py')