#1. Actions on the child imply an action on the Other.
#2. Actions on the child override the action on the Other.
#3. Actions on the child alter the action on the Other.
from sys import exit
import os

os.system('cls')

class Other(object):

	def override(self):
		print "Other override()"
		
	def implicit(self):
		print "Other implicit()"
		
	def altered(self):
		print "Other altered()"

class Child(object):
	def __init__(self):
		self.other = Other()
	
	def override(self):
		print "CHILD override()"
		
	def implicit(self):
		self.other.implicit()
		
	def altered(self):
		print "CHILD, before Other altered()"
		self.other.altered()
		print "CHILD, after Other altered()"

son = Child()
son.implicit()
son.override()
son.altered()

# class SuperFun(Child, BadStuff):
#	pass

#SuperFun inherits from classes Child and BadStuff
#Python uses "Method Resolution Order (MRO)" and an
#algorith called C3 