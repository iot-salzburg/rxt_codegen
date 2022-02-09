#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET

#--------------------------------------------
# Class to hold infos of one block
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
class XML_BlocklyProject_Parser():

	def __init__(self, fileName):
		self.tree = ET.parse(fileName)
		self.root = self.tree.getroot()
		self.listBlocks = []
		
	def getList(self):
		return self.listBlocks

	# read the assets involved in the script
	def readAssets(self):

		print ("-----------------------------------------------------")
		print ("Searching for all involved assets...")
		print ("-----------------------------------------------------")
		for asset in self.root:
			print ("Found involved Asset with following tag and attrib: ")
			print (asset.tag, asset.attrib)


	# read all blocks at once
	def readBlocks(self):

		print ("-----------------------------------------------------")
		print ("Parsing XML Tree searching for blocks...")
		print ("-----------------------------------------------------")

		blockCounter = 0
		self.listBlocks.append(SimpleBlockEntry("", [],[],[]))
	
		for entry in self.tree.iter():
				
			if(entry.tag=="{https://developers.google.com/blockly/xml}next" or entry.tag=="{https://developers.google.com/blockly/xml}statement"):
				print ("Found <next>-attribute")
				blockCounter += 1
				self.listBlocks.append(SimpleBlockEntry("", [],[],[]))
				
			elif(entry.tag=="{https://developers.google.com/blockly/xml}block"):
				print ("Found <block>-attribute with type = " + entry.attrib.get('type') + " and 'id = " + entry.attrib.get('id'))
				self.listBlocks[blockCounter].blockName.append(entry.attrib.get('type'))
					
			elif(entry.tag=="{https://developers.google.com/blockly/xml}value"): 
				print ("Found <value>-attribute with name = " + entry.attrib.get('name'))
				self.listBlocks[blockCounter].blockSlotName.append(entry.attrib.get('name'))
				
			elif(entry.tag=="{https://developers.google.com/blockly/xml}field"):
				print ("Found <field>-attribute with name = " + entry.attrib.get('name'))	
				self.listBlocks[blockCounter].blockSlotValue.append(entry.text)	
				
			else:
				print("Warning: Found an XML element that is unknown and unhandled!")

		# now put everything in order assigned to correct asset
		self.assignBlocksToAssets()
			

	# assign all blocks to an asset
	def assignBlocksToAssets(self):
	
		#for block in self.listBlocks:
		#	for name in block.blockName:
		#		print(name)
		#	print (';;')

		
		# assign blocks
		assetName = ""
		for entry in self.listBlocks:
			
			if(entry.blockName[0] == "SetAsset"):
				assetName = entry.blockSlotValue[0]
			
			entry.assetName = assetName
			print('\nFound entry: ' + entry.assetName + '; ' + entry.blockName[0] + '; ' + entry.blockSlotValue[0])
				
		# remove asset blocks
		for entry in self.listBlocks:

			if(entry.blockName[0] == "SetAsset"):
				self.listBlocks.remove(entry)

			
			
			
			
  
