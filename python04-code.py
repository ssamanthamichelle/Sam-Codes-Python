"""
	HEY GUYS, it's me SAM~

	this is the code from the
	Fourth Video in the Series Where I Teach Python
	on my youtube channel, Sam Codes

	feel free to download and run this!

	byeeee ;)
"""


def years_to_100():

	age = int(input("How old are you? "))

	if age <= 100:

		difference = 100 - age
		#years = str(difference)

		#print("You have " + years + " years until you turn 100")

		#instead...
		print("You have " + str(difference) + " years until you turn 100")

		
	else: #age > 100

		print("You already passed 100!")

#try entering different ages to see the different outputs
# ex, 22, 100, 102

years_to_100()

print("\n\n")

years_to_100()

print("\n\n")

years_to_100()

print("\n\n")
