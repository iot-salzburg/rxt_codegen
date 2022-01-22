#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('../input/example_oliver.xml')
root = tree.getroot()

#--------------------------------------------
# Class to hold infos of one block
#--------------------------------------------
class SimpleBlockEntry():	

	def __init__(self, blockName, blockSlotName, blockSlotValue):
		self.blockName = blockName
		self.blockSlotName = blockSlotName
		self.blockSlotValue = blockSlotValue

#--------------------------------------------
# Class to parse XML File from Blockly
#--------------------------------------------
class XML_BlocklyProject_Parser():

	# read the assets involved in the script
	def readAssets(self):

		print ("-----------------------------------------------------")
		print ("Searching for all involved assets...")
		print ("-----------------------------------------------------")
		for asset in root:
			print ("Found involved Asset with following tag and attrib: ")
			print (asset.tag, asset.attrib)

	# read all blocks at once
	def readBlocks(self):

		print ("-----------------------------------------------------")
		print ("Parsing XML Tree searching for blocks...")
		print ("-----------------------------------------------------")
		listBlocks = [] 
		blockCounter = 0
		listBlocks.append(SimpleBlockEntry("","",""))
	
		for entry in tree.iter():
				
			if(entry.tag=="{https://developers.google.com/blockly/xml}next"):
				print ("Found <next>-attribute")
				blockCounter += 1
				listBlocks.append(SimpleBlockEntry("","",""))
			elif(entry.tag=="{https://developers.google.com/blockly/xml}block"):
				print ("Found <block>-attribute with type = " + entry.attrib.get('type') + " and 'id = " + entry.attrib.get('id'))
				#print(entry.attrib)
				listBlocks[blockCounter].blockName += (entry.attrib.get('type') + ';')
			elif(entry.tag=="{https://developers.google.com/blockly/xml}value"): 
				print ("Found <value>-attribute with name = " + entry.attrib.get('name'))
				#print(entry.attrib)
				listBlocks[blockCounter].blockSlotName += (entry.attrib.get('name') + ';')
			elif(entry.tag=="{https://developers.google.com/blockly/xml}field"):
				print ("Found <field>-attribute with name = " + entry.attrib.get('name'))
				#print(entry.attrib)	
				listBlocks[blockCounter].blockSlotValue += (entry.text + ';')				
			else:
				print("Warning: Found an XML element that is unknown and unhandled!")

		return listBlocks
			
			 
  
