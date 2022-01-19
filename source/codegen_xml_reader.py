#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('../input/example.xml')
root = tree.getroot()

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
		
	print ("-----------------------------------------------------")
	print ("Parsing XML Tree searching for blocks...")
	print ("-----------------------------------------------------")
	for all_elements in tree.iter():
		
		for entry in all_elements:
				
			if(entry.tag=="{https://developers.google.com/blockly/xml}next"):  
				continue # next blocks not needed
			elif(entry.tag=="{https://developers.google.com/blockly/xml}block"):
				print ("Found <block>-attribute with type = " + entry.attrib.get('type') + " and 'id = " + entry.attrib.get('id'))
				print(entry.attrib)
			elif(entry.tag=="{https://developers.google.com/blockly/xml}value"): 
				print ("Found <value>-attribute with name = " + entry.attrib.get('name'))
				print(entry.attrib)			
			elif(entry.tag=="{https://developers.google.com/blockly/xml}field"):
				print ("Found <field>-attribute with name = " + entry.attrib.get('name'))
				print(entry.attrib)			
			else:
				print("Warning: Found an XML element that is unknown and unhandled!")

			
			 
  
