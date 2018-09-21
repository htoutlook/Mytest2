#1. Actions on the child imply an action on the parent.
#2. Actions on the child override the action on the parent.
#3. Actions on the child alter the action on the parent.
from sys import exit
import os

os.system('cls')

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, before parent altered()"
		super(Child, self).altered()
		print "CHILD, after parent altered()"


dad.altered()
son.altered()