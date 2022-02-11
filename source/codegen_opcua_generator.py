#!/usr/bin/env python
# coding=utf-8
import sys, string, os, shutil
import codegen_generator_helper
		
#--------------------------------------------
# Class to hold infos that should get created
#--------------------------------------------
class OPCUAGeneratorClass():

	def __init__(self, clientString, listBlocks):
		self.clientString = clientString
		self.listBlocks = listBlocks
	
	def dump_all(self, filename):

		if os.path.exists(os.path.dirname(filename)):
			shutil.rmtree(os.path.dirname(filename)) # recursive remove of dir and all files

		for blocks in self.listBlocks:
			assetName = blocks[0].assetName.lower()
			self.dump_self(filename + assetName + ".py", assetName, blocks)

	def dump_self(self, filename, assetName, blocks):
	
		# imports and Co
		self.c = codegen_generator_helper.GeneratorHelper()
		self.c.begin(tab="    ")
		self.c.write('TODO: Generate OPCUA')
		
		# TODO
		
		# write to filestream
		os.makedirs(os.path.dirname(filename), exist_ok=True) # Note: only works in Python 3.6(!)
		f = open(filename,'w')
		f.write(self.c.end())
		f.close()