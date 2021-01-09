#Sam Codes

"""

	HEY GUYS, it's me SAM

	this is the code from Python 02 on my youtube channel... Sam Codes

	feel free to download and run this!

	byeeee

	;)

"""

#printing a few lines to make the output look a bit nicer
# \n means new line
print("\n")
print("-------------------------------------")
print("Result from first program :")
print("\n")


######################
#Program which compares two numbers, a and b, and
#prints a message indicating whether or not they are equal

a = 5
b = 10

if a == b:
	print("the numbers are equal")
else:
	print("the numbers are not equal")



#formatting
print("\n")
print("-------------------------------------")
print("Result from are_equal() :")
print("\n")



##########################
#Same program but turned into a function~
#also I'm changing the variable names to make it less confusing


def are_equal(x, y):

	if x == y:
		print("the numbers are equal")
	else:
		print("the numbers are not equal")


#calling our function
are_equal(10, 10)

#formatting
print("\n")
print("-------------------------------------")


###################################
#Program which compares two numbers
#prints a message indicating whether:
#the two numbers are equal
#the first number is less than the second number
#the first number is greater than the second number

print("Result from compare_numbers() :")
print("\n")


def compare_numbers(first, second):

	if first == second:
		print("the numbers are equal")
	elif first < second:
		print("first number is less than second number")
	else:
		print("first number is greater than second number")

	#printing a message to let us know that everything went well
	print("program complete")


#calling our function compare_numbers
compare_numbers(12, 2)

print("\n") #formatting


