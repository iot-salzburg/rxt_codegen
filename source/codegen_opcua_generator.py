#!/usr/bin/env python
# coding=utf-8
import sys, string
import codegen_generator_helper
		
#--------------------------------------------
# Class to hold infos that should get created
#--------------------------------------------
class OPCUAGeneratorClass():

	def __init__(self, clientString, listBlocks):
		self.clientString = clientString
		self.listBlocks = listBlocks
	
	def dump_all(self, filename):

		for blocks in self.listBlocks:
			self.dump_self(filename + blocks[0].assetName.lower() + ".py", blocks)

	def dump_self(self, filename):
	
		# imports and Co
		self.c = codegen_generator_helper.GeneratorHelper()
		self.c.begin(tab="    ")
		self.c.write('TODO: Generate OPCUA')
		
		# TODO
		
		# write to filestream
		f = open(filename,'w')
		f.write(self.c.end())
		f.close()