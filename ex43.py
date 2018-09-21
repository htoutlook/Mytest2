from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not configured.  Subclass it and implement enter()"
			exit(1)
			
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Death(Scene):
	quips = ]
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a loooser.",
		"I have a small pupy that's better."
	]
	
	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):
	def enter(self):
		print "Gothons invaded your ship"
	
	action = raw_input("> ")
	
	if action == "shoot":
		print "You shoot at em like a boss"
		return 'death'
	elif action == "dodge":
		print "You dodge like a boss"
	elif action == "joke":
		print "You tell em a joke"
	else:
		print "NO NO NO"
		return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print "Inside of the weapon armory"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guesses = 0
		
		while guess != code and guesses < 10:
			print "BZZZZZEDDDD"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "Access granted.  Container opens"
			return 'the_bridge'
		else:
			print "Access denied.  Container stays locked.  Prepare to get blasted."
			return 'death'
			
class TheBridge(Scene):
	def enter(self):
		print "You're in the bridge with the bomb"
		action = raw_input("> ")
		
		if action == "throw bomb":
			print "You throw the bomb"
			return 'death'
		elif action == "set bomb down":
			print "You set the bomb down"
			return 'escape_pod'
		else:
			print "NO NO NO"
			return 'the_bridge'
			
class EscapePod(Scene):
	def enter(self):
		print "You go into the escape pod"
		print "Pick the pod"
		good_pod = randint(1,5)
		gues = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s" % guess
			print "It blows up"
			return 'death'
		else:
			print "You jump into pod %s" % guess
			print "The pod launches successfully"
			return 'finished'
			
			
		