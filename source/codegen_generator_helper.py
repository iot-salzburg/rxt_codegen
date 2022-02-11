#!/usr/bin/env python

#--------------------------------------------
# Class to create python code
#--------------------------------------------
# Author: SRFG, Mathias Schmoigl-Tonis
# Project: ROBxTASK
# Date: Q1-Q2 2022
#--------------------------------------------
class GeneratorHelper:

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