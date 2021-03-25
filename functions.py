import random



def rollDie():
	'''This rolls a die.
	
	We use a random number generator and print'''
	die = random.randint(1,6)
	#print ("You rolled " + str(die))
	return die
	

def playWithIteration(n):
	print ("Running playWithIteration-" + str(n) )
	#know when to stop
	if (n==0):
		print ("\tn is 0 so we stop and return 0")
		return 0;
	
	currentMax=0
	for i in range (0,n):
		r = rollDie()
		if (r>currentMax):
			currentMax=r
	print ("\t The max on round " + str(n) + " is " + str(currentMax))
	#add to total
	print ("\t Now calling playWithIteration of " + str(n-1))
	return currentMax + playWithIteration(n-1)



total = playWithIteration(5)
print ("The total is " + str(total))

#this plays the game with a loop
#this is a function to roll a die multiple times
# def rollNKeepMax(n):
# 	'''This rolls n dice and keeps the max.'''
# 	max=0
# 	for i in range (0,n):
# 		r = rollDie()
# 		if (r>max):
# 			max=r
# 	#print (max)
# 	return max

# total=0
# for round in range (1,6):
# 	print ("Round " + str(round))
# 	maxDie = rollNKeepMax(6-round)
# 	total = total+maxDie
# 	print ("The max die is " + str(maxDie))
# 	#print ("Running total is " + str(total))
# print ("Your score is " + str(total))

#this rolls a die 3 times and picks the biggest val
# r1=rollDie()
# r2=rollDie()
# r3=rollDie()
# 
# if (r1>r2 and r1>r3):
# 	print (r1)
# elif (r2>r3):
# 	print (r2)
# else:
# 	print (r3)
	






#print (rollDie.__doc__)