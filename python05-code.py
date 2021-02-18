"""
	HEY GUYS, it's me SAM~

	this is the code from the Python 05 video on my youtube channel Sam Codes

	feel free to download and run this program!

	byeee ;)

"""


def questions():

	q1 = input("Have you experienced any of the following symptoms in the past 48 hrs- fever or chills, cough, shortness of breath or difficulty breathing, fatigue, muscle aches, headache, new loss of taste or smell, sore throat, congestion or runny nose, nausea or vomiting, diarrhea?")

	if q1 == "yes":
		q1 = True
	else:
		q1 = False


	q2 = input("Within the past 14 days have you been in close physical contact (6ft or closer for a cumulative total of 15 minutes) with- anyone who is know to have laboratory-confirmed COVID-19 or anyone who has any symptoms consistent with COVID-19?")

	if q2 == "yes":
		q2 = True
	else:
		q2 = False
	

	q3 = input("Are you isolating or quarantining because you may have been exposed to a person with covid-19 or are you worried that you may be sick with covid-19?")

	if q3 == "yes":
		q3 = True
	else:
		q3 = False


	q4 = input("Are you currently waiting on the results of a covid-19 test?")

	if q4 == "yes":
		q4 = True
	else:
		q4 = False


	if q1 or q2 or q3 or q4:
		print("no u can't come in")
	else:
		print("Come in!")


questions()

