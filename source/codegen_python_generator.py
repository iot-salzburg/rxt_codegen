#!/usr/bin/env python
# coding=utf-8
import sys, string

#--------------------------------------------
# Class to create python code
#--------------------------------------------
class CodeGeneratorBackend:

	def begin(self, tab="\t"):
		self.code = []
		self.tab = tab
		self.level = 0

	def end(self):
		return "".join(self.code)

	def write(self, string):
		self.code.append(self.tab * self.level + string)

	def indent(self):
		self.level = self.level + 1

	def dedent(self):
		#if self.level == 0:
		#    raise SyntaxError, "internal error in code generator"
		self.level = self.level - 1

#--------------------------------------------
# Class to hold infos that should get created
#--------------------------------------------
class GeneratorClass_StaticHeader():

	def __init__(self, clientString):
		self.clientString = clientString

	def dump_self(self, filename):
		
		# imports and Co
		self.c = CodeGeneratorBackend()
		self.c.begin(tab="    ")
		self.c.write('#! /usr/bin/env python\n\n')
		self.c.write('import rospy\n')
		self.c.write('import time\n\n')
		self.c.write('import actionlib # Brings in the SimpleActionClient\n')
		self.c.write('import rxt_skills_qbo.msg # Brings in the messages used by the qbo actions\n\n')	
		
		# function: send_ROSActionRequest_WithGoal
		self.c.write('# client request helper function\n')
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
		self.c.write('# main function\n')
		self.c.write('if __name__ == \'__main__\':\n')
		self.c.indent()
		self.c.write('try:\n')
		
		# TODO: create blocks!!!
		self.c.indent()
		#TODO: generated blocks should go here!!!
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
    
  
