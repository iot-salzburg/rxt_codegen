#!/usr/bin/env python
# coding=utf-8
import sys, string
import codegen_generator_helper

#--------------------------------------------
# Class to hold infos that should get created
#--------------------------------------------
class ROSGeneratorClass():

	def __init__(self, clientString, listBlocks):
		self.clientString = clientString
		self.listBlocks = listBlocks

	def dump_self(self, filename):
		
		# imports and Co
		self.c = codegen_generator_helper.GeneratorHelper()
		self.c.begin(tab="    ")
		self.c.write('#! /usr/bin/env python\n\n')
		self.c.write('import rospy\n')
		self.c.write('import time\n\n')
		self.c.write('import actionlib # Brings in the SimpleActionClient\n')
		self.c.write('import rxt_skills_qbo.msg # Brings in the messages used by the qbo actions\n\n')	
		
		# function: send_ROSActionRequest_WithGoal
		self.c.write('#--------------------------------------------------------------------------------------\n')
		self.c.write('# client request helper function\n')
		self.c.write('#--------------------------------------------------------------------------------------\n')
		self.c.write('def send_ROSActionRequest_WithGoal(skillName, skillMsgType, skillGoal):\n\n')
		self.c.indent()
		self.c.write('rospy.init_node('+ self.clientString +') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS\n\n')
		self.c.write('client = actionlib.SimpleActionClient(skillName, skillMsgType) # Creates SimpleActionClient with skillMsgType action type\n')
		self.c.write('client.wait_for_server() # Waits until the action server has started up and started listening for goals\n')
		self.c.write('client.send_goal(skillGoal) # Sends the goal to the action server\n')
		self.c.write('client.wait_for_result() # Waits for the server to finish performing the action\n\n')
		self.c.write('return client.get_result() # Prints out the result (WaitForUserInputResult) of executing the action\n\n')
		self.c.dedent()	
		
		# function: main open
		self.c.write('#--------------------------------------------------------------------------------------\n')
		self.c.write('# main function\n')
		self.c.write('#--------------------------------------------------------------------------------------\n')
		self.c.write('if __name__ == \'__main__\':\n')
		self.c.indent()
		self.c.write('try:\n')
		
		# create all blocks read from XML
		self.c.indent()
		for block in self.listBlocks:
			self.c.write(block.blockName + '\n')
			self.c.write(block.blockSlotName + '\n')
			self.c.write(block.blockSlotValue + '\n\n')
		self.c.dedent()			
		
		# function: main close
		self.c.write('except rospy.ROSInterruptException:\n')
		self.c.indent()
		self.c.write('print(\"program interrupted before completion\")\n')
		self.c.dedent()	
		
		# write to filestream
		f = open(filename,'w')
		f.write(self.c.end())
		f.close()




	