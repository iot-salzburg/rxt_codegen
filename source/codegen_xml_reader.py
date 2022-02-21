#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET

#--------------------------------------------
# Helper class to hold infos of one block
#--------------------------------------------
class SimpleBlockEntry():	

	def __init__(self, assetName, blockName, blockSlotName, blockSlotValue):
		self.assetName = assetName
		self.blockName = blockName
		self.blockSlotName = blockSlotName
		self.blockSlotValue = blockSlotValue

#--------------------------------------------
# Class to parse XML File from Blockly
#--------------------------------------------
# Author: SRFG, Mathias Schmoigl-Tonis
# Project: ROBxTASK
# Date: Q1-Q2 2022
#--------------------------------------------
class XML_BlocklyProject_Parser():

	#--------------------------------------------
	# CTOR: init class with variable members
	#--------------------------------------------
	def __init__(self, fileName):
		self.tree = ET.parse(fileName)
		self.root = self.tree.getroot()
		self.listBlocks = []

	#--------------------------------------------
	# read the assets involved in the script
	#--------------------------------------------
	def readAssets(self):

		print ("Searching for all involved assets...")
		for asset in self.root:
			print ("-----------------------------------------------------")
			print ("Found involved Asset with following tag and attrib: ")		
			print (asset.tag, asset.attrib)
			print ("-----------------------------------------------------")

			blocks = self.readBlocks(asset)
			self.listBlocks.append(blocks)

	#--------------------------------------------
	# read all blocks at once
	#--------------------------------------------
	def readBlocks(self, asset):

		print ("Parsing XML Tree searching for blocks...")

		blockCounter = 0
		blocks = []
		blocks.append(SimpleBlockEntry("", [],[],[]))
		statementBlockCounter = 0
	
		for entry in asset.iter():
				
			if(entry.tag=="{https://developers.google.com/blockly/xml}next"):
				print ("Found <next>-attribute")

				# Need to count down number of blocks within Statement (Loop or Selection)
				# Add a Stament End Tag, when counter is zero again
				if(statementBlockCounter > 0):
					statementBlockCounter -= 1
					if (statementBlockCounter == 0):
						blockCounter += 1
						blocks.append(SimpleBlockEntry("", ["STATEMENT_ENDTAG"],["STATEMENT_ENDTAG"],["STATEMENT_ENDTAG"]))

				# normally start a new block
				blockCounter += 1
				blocks.append(SimpleBlockEntry("", [],[],[]))
			
			elif(entry.tag=="{https://developers.google.com/blockly/xml}statement"):
				print ("Found <statement>-attribute")

				# normally start a new block
				blockCounter += 1
				blocks.append(SimpleBlockEntry("", [],[],[]))

				# we are starting a statement and need to find the end of Selection or Loop
				# count (nr of "next"-children + 1) to get actual nr of subnodes of statement block
				statementBlockCounter = len(list(entry.iter('{https://developers.google.com/blockly/xml}next'))) + 1

			elif(entry.tag=="{https://developers.google.com/blockly/xml}block"):
				print ("Found <block>-attribute with type = " + entry.attrib.get('type') + " and 'id = " + entry.attrib.get('id'))
				blocks[blockCounter].blockName.append(entry.attrib.get('type'))
					
			elif(entry.tag=="{https://developers.google.com/blockly/xml}value"): 
				print ("Found <value>-attribute with name = " + entry.attrib.get('name'))
				blocks[blockCounter].blockSlotName.append(entry.attrib.get('name'))
				
			elif(entry.tag=="{https://developers.google.com/blockly/xml}field"):
				print ("Found <field>-attribute with name = " + entry.attrib.get('name'))	
				blocks[blockCounter].blockSlotValue.append(entry.text)	
				
			else:
				print("Warning: Found an XML element that is unknown and unhandled!")

		self.assignBlocksToAssets(blocks) # now put everything in order assigned to correct asset
		return blocks
			
	#--------------------------------------------
	# assign all blocks to an asset
	#--------------------------------------------
	def assignBlocksToAssets(self, blocks):
		
		# assign blocks
		assetName = ""
		for entry in blocks:
			
			if(entry.blockName[0] == "SetAsset"):
				assetName = entry.blockSlotValue[0]
			
			entry.assetName = assetName
			#print('\nFound entry: ' + entry.assetName + '; ' + entry.blockName[0] + '; ' + entry.blockSlotValue[0])
				
		# remove asset blocks
		for entry in blocks:

			if(entry.blockName[0] == "SetAsset"):
				blocks.remove(entry)

	#--------------------------------------------
	# GETTER: return listBlock member variable
	#--------------------------------------------
	def getList(self):
		return self.listBlocks