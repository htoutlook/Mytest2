
from sys import exit
import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex35a" #116
print "================================================\n"

nextn = 0

while True:
	next = raw_input("> ")
	
	#next != "jj"
	if "jj" in next:
		break
	elif "123" in next:
		print next	
	else:
		nextn += 1
		print nextn
		
print "\n================================================"
print "\t\tEND"
print "================================================\n"

