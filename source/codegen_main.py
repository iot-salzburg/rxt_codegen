#!/usr/bin/env python
# coding=utf-8
import codegen_xml_reader
import codegen_python_generator

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
if __name__== "__main__":

	print ("Trying to parse XML input file now...")
	
	p = codegen_python_generator.GeneratorClass_StaticHeader('qbo_client_py')
	p.dump_self('../output/auto_generated.py')
	
	codegen_xml_reader.readAssets()
	codegen_xml_reader.readBlocks()