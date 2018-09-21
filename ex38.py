
from sys import exit
import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex38 129"
print "================================================\n"


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy", "L", "C", "Airwaves"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	print "%s" % stuff
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print'#'.join(stuff[3:5]) 

print "\n================================================"
print "\t\tEND"
print "================================================\n"

