import random

class Game:
	def __init__(self):
		print("Starting game")
		self.playerList=[]
		self.winningPlayer = 0
		self.numberOfPlayers = int(input("How many players are playing?  "))
		for z in range (1, self.numberOfPlayers +1):
			self.playerList.append(Player(z))
		


	def playGame(self):
		print("This is the Game class's playGame function")


	def rollDie(self):
		return random.randint(1,6)

class TTT(Game):
	"""docstring for TTT"""
	def __init__(self):
		Game.__init__(self)
		#Check we only have 2 players or fewer
		self.playGame()

	def playGame(self):
		print("| | |\n_____\n| | |\n_____\n| | |")
		
		

class DiceGame(Game):
	def __init__(self):
		Game.__init__(self)
		#do other stuff if you wish
		print("Initialized")
		self.playGame()

	def playGame(self):
		#Game.playGame(self)
		print("Starting game play")
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

		self.playGame()

class Player:
	def __init__(self,number):
		self.name = input("What is your name?" + str(number))
		self.score = -1


p = TTT()
