import random
#game
#dice  - number of players, roll die, highest score wins

class Game:
	def __init__(self):
		self.playerList=[]
		self.winningPlayerNumber=0
		self.numberOfPlayers = int(input("How many players? "))
		for i in range(1,self.numberOfPlayers+1):
			self.playerList.append(Player(i))
		self.playGame()

	def playGame(self):
		playerNum=0
		for player in self.playerList:
			input(player.name + ", it's your turn. Hit enter to roll.")
			player.score = self.rollDie()
			print (player.name + " rolled " + str(player.score))
			#track winner
			if (player.score>self.playerList[self.winningPlayerNumber].score):
				self.winningPlayerNumber = playerNum
				print (player.name +  " is the current winner.")
			playerNum = playerNum+1
		print(self.playerList[self.winningPlayerNumber].name + " wins")
	
	def rollDie(self):
		return random.randint(1,6)

class Player:
	def __init__(self,number):
		self.name = input("Enter your name, Player " + str(number) + ": ")
		self.score=-1
		
g = Game()