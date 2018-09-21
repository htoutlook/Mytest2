
from sys import exit
import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex35" #116
print "================================================\n"

#gold room function
def gold_room():
	print "This room is full of gold.  How much do you take?"
	
	next = raw_input("> ")
	
	#checks if 0 or 1 are in vari next
	if "0" in next or "1" in next:
		
		#assign value and convert next to int
		how_much = int(next)
	else:
		#if 1 or 0 are not in next call dead() and pass text
		dead("Man, learn to type a number. " + next)
	
	
	if how_much < 50:
		print "Nice, you're not greedy, you win! " + next
		#call ext()
		exit(0)
	else:
		#how much is greater than 49
		#call dead() and pass text as WHY
		dead("You greedy poop! " + next)
		
#bear room function
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face")
		elif next == "taunt bear" and not bear_moved:
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets mad and chews your leg")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

def cthulhu_room():
	print "Here you see the evil Cthulhu"
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room"
	print "There is a door to your right and left"
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	#if next == "left":
	if "left" in next:
		bear_room()
	#elif next == "right":
	elif "right" in next:
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")
		
start()
		
print "\n================================================"
print "\t\tEND"
print "================================================\n"

