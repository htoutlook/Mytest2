
from sys import exit
import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex39 133"
print "================================================\n"

#create a maping of state abbreviation

def jj():
	print '-' * 30

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
	'Texas': 'TX',
	'WA': 'Washington'
}

#create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	'TX': 'San Antonio',
	'WA': 'Seattle'
}
	
	
xstate = raw_input("> ")
print states.get(xstate), ", ", cities.get(xstate)
#print states[xstate], ", ", cities[states[xstate]]

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
jj()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
print "Enter a state abbrev"


#print some states
jj()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
jj()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
jj()
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
#print every city in state
jj()
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
#now do both at the same time
jj()
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
#safely get an abbreviation by state that might not be there
jj()
state = states.get('Arizona', None)

if not state:
	print "Sorry, no Arizona"

#get a city with a default values
jj()
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city



print "\n================================================"
print "\t\tEND"
print "================================================\n"

