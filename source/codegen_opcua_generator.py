#!/usr/bin/env python
# coding=utf-8
import sys, string, os, shutil
import codegen_generator_helper
		
#--------------------------------------------
# Class to hold infos that should get created
#--------------------------------------------
# Author: SRFG, Mathias Schmoigl-Tonis
# Project: ROBxTASK
# Date: Q1-Q2 2022
#--------------------------------------------
class OPCUAGeneratorClass():

	#--------------------------------------------
	# CTOR: init class with variable members
	#--------------------------------------------
	def __init__(self, clientString, listBlocks):
		self.clientString = clientString
		self.listBlocks = listBlocks
	
	#--------------------------------------------
	# dump all blocks of all assets to files
	#--------------------------------------------
	def dump_all(self, filename):

		if os.path.exists(os.path.dirname(filename)):
			shutil.rmtree(os.path.dirname(filename)) # recursive remove of dir and all files

		for blocks in self.listBlocks:
			assetName = blocks[0].assetName.lower()
			self.dump_self(filename + "agent_rxta_" + assetName + "_sim_01.py", assetName, blocks)

	#--------------------------------------------
	# dump all blocks of one asset to file
	#--------------------------------------------
	def dump_self(self, filename, assetName, blocks):
	
		# imports and Co
		self.c = codegen_generator_helper.GeneratorHelper()
		self.c.begin(tab="    ")
		self.c.write('import asyncio\n')
		self.c.write('from logging import setLogRecordFactory\n')
		self.c.write('import robXTask.rxtx_helpers as rxtx_helpers\n\n')
		self.c.write('import rxta_ARTI_Sim as rxta_ARTI_Sim\n\n')

		# main routine
		self.c.write('async def startRobXTask():\n')
		self.c.indent()
		self.c.write('print("*** startRobXTask")\n')
		self.c.write('# This is the main-code - place any startup things here as needed...\n\n')
		self.c.dedent()	
		
		# ---------------------------------------------------------------------------------------
		# TODO: the following lines are not yet finished, just preview

		# async call 1
		self.c.write('async def on_rxte__message__FetchDrink__rxtx_helpers(messages):\n')
		self.c.indent()
		self.c.write('async for message in messages:\n')
		self.c.indent()
		self.c.write('await rxtx_helpers.logMessageReceived(message)\n')
		self.c.write('print("*** on_rxte__message__FetchWater__rxtx_helpers()")\n')
		self.c.write('sDrink = str(message.payload.decode("utf-8")).strip()\n')
		self.c.write('print("got Message: " + sDrink)\n')
		self.c.write('await rxtx_helpers.log(rxtx_helpers.enLogType.BLOCKLY,"rxta_ARTI_Sim.MoveToLocationARTI(Goal_Roboter)")\n')
		self.c.write('await rxta_ARTI_Sim.MoveToLocationARTI("Goal_Roboter")\n')
		self.c.write('await rxtx_helpers.sendMessage("GrabDrink", sDrink)\n\n')
		self.c.dedent()
		self.c.dedent()

		# async call 2
		self.c.write('async def on_rxte__message__DrinkGrabbed__rxtx_helpers(messages):\n')
		self.c.indent()
		self.c.write('async for message in messages:\n')
		self.c.indent()
		self.c.write('await rxtx_helpers.logMessageReceived(message)\n')
		self.c.write('print("*** on_rxte__message__DrinkGrabbed__rxtx_helpers()")\n')
		self.c.write('sDrink = str(message.payload.decode("utf-8")).strip()\n')
		self.c.write('print("got Message: " + sDrink)\n')
		self.c.write('await rxtx_helpers.log(rxtx_helpers.enLogType.BLOCKLY,"rxta_ARTI_Sim.MoveToLocationARTI(Goal_Couch)")\n')
		self.c.write('await rxta_ARTI_Sim.MoveToLocationARTI("Goal_Couch")\n')
		self.c.write('await rxtx_helpers.sendMessage("DrinkFetched", sDrink)\n\n')
		self.c.dedent()
		self.c.dedent()

		# start async
		self.c.write('rxtx_helpers.startAsync()\n')

		# TODO : end section
		# ---------------------------------------------------------------------------------------

		# write to filestream
		os.makedirs(os.path.dirname(filename), exist_ok=True) # Note: only works in Python 3.6(!)
		f = open(filename,'w')
		f.write(self.c.end())
		f.close()