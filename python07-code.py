"""
	hey guys, it's me SAM~

	this is the code from my youtube video on string manipulation!

	feel free to download and run this!

	***remember that string indexing begins at index zer0!

	if a string is n characters long
	first index will be zero
	last index will be n-1

	;)

"""

var = "hello friends"

#Getting one character

#first character in string
var[0]

#last character in var
var[12]

#last character in any string, no matter how long
var[-1]


#Getting multiple characters
#RECALL- start is inclusive, stop index is exclusive
# my_string[start:stop]

#just 'hello'
var[0:5]

#zero is implied if no start index
var[:5]

#just 'friends'
var[6:12]

#if no stop index is specified, python will just go to the end
var[6:]

#everything but the last character
var[:-1]


# my_string[start:stop:step]

#every other character
var[::2]

#the whole string backwards
var[::-1]


#the len() function

my_string = "this is my string"
length = len(my_string)

my_string[0] #first index

my_string[length-1] #last index
#OR
my_string[len(my_string) - 1] #last index





