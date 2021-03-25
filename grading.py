
#grade = int(input("Enter grade"))
last_grade = 0
while True:
	last_grade +=1
	grade = int(input("Enter grade: "))

	if (grade >=90):
		print("Yay! You have got an A grade")

	elif grade in range (80,89):
		print("Good job! You have got a B grade")

	elif grade in range (70,79):
		print("Good try! You have got a C grade")


	elif grade in range (60,69):
		print("Do better next time bro! You have got a D grade")

	else:
		print("I'm sorry but you gonna have to retake this class dude!")

	


