quizzes = int(input("How many quizzes : "))
score_list = list()

for i in range(quizzes):
	#takes input as string
	score = input("Enter score for  quiz number: ")
	#convert to float
	score.float()
	#appending content to list
	score_list.append(score)
print(score_list)

	


