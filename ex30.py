import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex30"
print "================================================\n"

people = int(raw_input("People = "))
cars = int(raw_input("Cars = "))
buses = int(raw_input("Buses = "))

if cars > people:
	print "We should take the cars"
elif cars < people:
	print "We should not take the cars"
else:
	print "We can't decide"

if buses > cars:
	print "That's too many buses"
elif buses < cars:
	print "Maybe we could take the buses"
else:
	print "We still can't decide"
	
if people > buses:
	print "Alright, let's just take the buses"
else:
	print "Fine, let's stay home"


print "================================================"
print "\t\tEND"
print "================================================\n\n"