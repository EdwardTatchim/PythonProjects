import random

class Game:
	def __init__(self):
		print("Starting game")
		self.playerList=[]
		self.winningPlayer = 0
		self.numberOfPlayers = int(input("How many players are playing?  "))
		for z in range (1, self.numberOfPlayers +1):
			self.playerList.append(Player(z))

		self.playGame()


	def playGame(self):
		playNum = 0
		for playa in self.playerList:
			input(playa.name + ", it's your turn. Hit enter to roll. ")
			playa.score = self.rollDie()
			print(playa.name + " rolled " + str(playa.score))
			#keep track of winner
			if(playa.score>self.playerList[self.winningPlayer].score):
				self.winningPlayer = playNum
				print(playa.name + " is the current winner. ")

			playNum +=1
		print(self.playerList[self.winningPlayer].name + " wins. ")



	def rollDie(self):
		return random.randint(1,6)



class Player:
	def __init__(self,number):
		self.name = input("What is your name?" + str(number))
		self.score = -1


p = Game()
