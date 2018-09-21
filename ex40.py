from random import randint

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there!"])
				
				
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells",
						"aaaaaaaaaaaaaaaaaaaaaaaaaaaa",
						"dddddddddddddddddddddddddddd",
						"zzzzzzzzzzzzzzzzzzzzzzzzzzzz"])
						
rambo = Song([randint(0,100),
			"=============",
			randint(0,100000),
			"-------------",
			randint(1000000,1000000000000),
			"_____________"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

rambo.sing_me_a_song()
