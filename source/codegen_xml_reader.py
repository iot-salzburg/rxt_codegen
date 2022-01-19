#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('../input/example.xml')
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
# fkt readAssets
#--------------------------------------------
def readAssets():
	
	print ("-----------------------------------------------------")
	print ("Searching for all involved assets...")
	print ("-----------------------------------------------------")
	for asset in root:
		print ("Found involved Asset with following tag and attrib: ")
		print (asset.tag, asset.attrib)

#--------------------------------------------
# fkt readBlocks
#--------------------------------------------
def readBlocks():

	listBlocks = [] 
		
	print ("-----------------------------------------------------")
	print ("Parsing XML Tree searching for blocks...")
	print ("-----------------------------------------------------")
	for all_elements in tree.iter():
		
		blockCounter = 0
		listBlocks.append(SimpleBlockEntry("","",""))
		
		for entry in all_elements:
				
			if(entry.tag=="{https://developers.google.com/blockly/xml}next"):
				print ("Found <next>-attribute")
				blockCounter += 1
				listBlocks.append(SimpleBlockEntry("","",""))
				print (blockCounter)
			elif(entry.tag=="{https://developers.google.com/blockly/xml}block"):
				print ("Found <block>-attribute with type = " + entry.attrib.get('type') + " and 'id = " + entry.attrib.get('id'))
				#print(entry.attrib)
				listBlocks[blockCounter].blockName = entry.attrib.get('type')
			elif(entry.tag=="{https://developers.google.com/blockly/xml}value"): 
				print ("Found <value>-attribute with name = " + entry.attrib.get('name'))
				#print(entry.attrib)
				listBlocks[blockCounter].blockSlotName = entry.attrib.get('name')
			elif(entry.tag=="{https://developers.google.com/blockly/xml}field"):
				print ("Found <field>-attribute with name = " + entry.attrib.get('name'))
				#print(entry.attrib)	
				listBlocks[blockCounter].blockSlotValue = entry.attrib.get('name')				
			else:
				print("Warning: Found an XML element that is unknown and unhandled!")
	#print(listBlocks)
	return listBlocks
			
			 
  
