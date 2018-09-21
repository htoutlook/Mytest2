#1. Actions on the child imply an action on the parent.
#2. Actions on the child override the action on the parent.
#3. Actions on the child alter the action on the parent.

class Parent(object):
	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()