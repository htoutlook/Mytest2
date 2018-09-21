#1. Actions on the child imply an action on the parent.
#2. Actions on the child override the action on the parent.
#3. Actions on the child alter the action on the parent.

class Parent(object):
	def override(self):
		print "PARENT override()"

class Child(Parent):
	def override(self):
		print "CHILD override()"
	
	

dad = Parent()
son = Child()

dad.override()
son.override()