import mystuff

#mystuff.apple()

#print mystuff.tangerine

class MyStuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years"
		self.jumpe = "zzzzzzzzzzzzzzzz"
		self.roo = "^_" * 20
		
	def apple(self):
		print "I am classy apples"
	
	def jump(self):
		print """
		This
		is
		from
		jump
		"""

thing = MyStuff()
thing.apple()

thing.jump()

print thing.roo
print thing.tangerine
print thing.roo
print thing.jumpe
print thing.roo


#dict style
mystuff['apples']

#module style
mystuff.apples()
print mystuff.tangerine

#class style
thing = MyStuff()
thing.apples
print thing.tangerine



