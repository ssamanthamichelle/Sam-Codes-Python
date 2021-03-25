"""

	hey guys, it's me SAM~

	here is the code for the two programs in my youtube video python 08

	feel free to download & run this!

	;)

"""


# first program
# only works for 1 string- my_string = '123 GO!'
# ... if you want to use a different string, have to modify function...
# not ideal :/
####################################
def print_chars1():

	my_string = '123 GO!'

	for char in my_string:
		print(char)


#calling first function
print_chars1()



# second program
# more useful because my_string isn't hard-coded
# can call function with different arguments
####################################
def print_chars(my_string):

	for char in my_string:
		print(char)


#calling second function
print_chars("this is my string!")


