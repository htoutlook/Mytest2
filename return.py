import os

os.system('pause')
os.system('cls')

xanswer = 0

def test():
	print "Make a choice?  1 or 2"
	xanswer = raw_input("> ")
	
	return xanswer

print xanswer
xanswer2 = test()
if xanswer2 == "1":
	test()
elif xanswer2 == "2":
	test()
else:
	print "Bye"