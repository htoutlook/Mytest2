import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex29"
print "================================================\n"

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats!"

if people > cats:
	print "Not too many cats"

if people < dogs:
	print "Drooled"
	
if people > dogs:
	print "Dry"
	
dogs += 5

if people >= dogs:
	print "People are greater or equal to dogs"
	
if people <= dogs:
	print "People are less or equal to dogs"
	
if people == dogs:
	print "People are dogs"

print "================================================"
print "\t\tEND"
print "================================================\n\n"