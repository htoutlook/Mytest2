def jj(xx, xi):
	i = 0
	numbers = []
	
	while i < xx:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + xi
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

xx = int(raw_input("Final number xx> "))
xi = int(raw_input("Increment xi> "))

jj(xx, xi)	