"""
	HEY GUYS, it's me SAM~

	this is the code from the Python 06 video on my youtube channel Sam Codes

	feel free to download and run this program!

	byeee ;)

"""


def questions():

	q1 = input("Have you experienced any of the following symptoms in the past 48 hrs- fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea?")

	q1 = to_bool(q1)


	q2 = input("Within the past 14 days have you been in close physical contact (6ft or closer for a cumulative total of 15 minutes) with- anyone who is know to have laboratory-confirmed COVID-19 or anyone who has any symptoms consistent with COVID-19?")

	q2 = to_bool(q2)
	

	q3 = input("Are you isolating or quarantining because you may have been exposed to a person with covid-19 or are you worried that you may be sick with covid-19?")

	q3 = to_bool(q3)


	q4 = input("Are you currently waiting on the results of a covid-19 test?")

	q4 = to_bool(q4)


	if q1 or q2 or q3 or q4:
		print("no u can't come in")
	else:
		print("Come in!")


#takes a string and returns a bool
def to_bool(answer):

	if answer == "yes":
		return True
	else:
		return False


questions()




