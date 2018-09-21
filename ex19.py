import os
os.system('cls')

print "\n================================================"
print "\t\tSTART ex19"
print "================================================\n"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

os.system('pause')
os.system('cls')
xcheese = int(raw_input("Enter the amount of cheese> "))
xcrack = int(raw_input("Enter the amount of crackers> "))

cheese_and_crackers(xcheese,xcrack)

print "================================================"
print "\t\tEND"
print "================================================\n\n"