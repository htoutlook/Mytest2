#1. Actions on the child imply an action on the parent.
#2. Actions on the child override the action on the parent.
#3. Actions on the child alter the action on the parent.
from sys import exit
import os

os.system('cls')

class Parent(object):

	def override(self):
		print "PARENT override()"
	def implicit(self):
		print "PARENT implicit()"
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"
	def implicit(self):
		print "CHILD implicit()"
	def altered(self):
		print "CHILD, before parent altered()"
		super(Child, self).altered()
		print "CHILD, after parent altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()