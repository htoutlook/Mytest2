import os

os.system('pause')
os.system('cls')

print "\n================================================"
print "\t\tSTART ex20"
print "================================================\n"

from sys import argv

script, input_file = argv
#READ THE FILE
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
		
#ARGV = LINE NUMBER, FILENAME
def print_a_line(line_count, f):
			#PRINT THE LINE X, PRINT THE TEXT FROM FILE AT LINE X
			print line_count, f.readline()

#SET CURRENT_FILE TO THE ARGV
current_file = open(input_file)

print "First let's print the whole file:\n"

#PRINT THE WHOLE FILE
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#PRINTS LINE 1 OF THE FILE
current_line = 1
print_a_line(current_line, current_file)

#PRINTS LINE 2 OF THE FILE
current_line += 1
print_a_line(current_line, current_file)

#PRINTS LINE 3 OF THE FILE
current_line += 4
print_a_line(current_line, current_file)

print "================================================"
print "\t\tEND"
print "================================================\n\n"