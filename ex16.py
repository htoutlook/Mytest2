from sys import argv

script, filename = argv

txt = filename
print "\n\n================================================"
print "\t\t         START ex16"
print "================================================\n"

print "We're going to erase %r." % filename

print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')
#'a' append
#'w' write
#'r' read

print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("\n")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target = open(filename)
print "\n\n"
print target.read()
print "And finally, we close it."
target.close()

print "================================================"
print "\t\t          END"
print "================================================\n\n"