import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex21"
print "================================================\n"

def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

#age is the RETURN value from add(a, b)
#a and b values are defined by the user and converted to INT
print "Add"
age = add(int(raw_input("A> ")), int(raw_input("B> ")))

#height is the RETURN value from subtract(a, b)
#a and b values are defined by the user and converted to INT
print "Subtract"
height = subtract(int(raw_input("A> ")),int(raw_input("B> ")))

#weight is the RETURN value from multiply(a, b)
#a and b values are defined by the user and converted to INT
print "Multiply"
weight = multiply(int(raw_input("A> ")),int(raw_input("B> ")))

#IQ is the RETURN value from divide(a, b)
#a and b values are defined by the user and converted to INT
print "Divide"
iq = divide(int(raw_input("A> ")),int(raw_input("B> ")))

print "\n\nAge: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "\n\nHere is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "\n\nThat becomes: ", what, "Can you do it by hand?"

print "================================================"
print "\t\tEND"
print "================================================\n\n"