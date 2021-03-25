#Question 1
import random

class Player:
	playerList = []

	def __init__(self,name):
		self.name = name
		self.position = 0
		#self.playerList.append(self.name)
		#print(self.playerList)
		Player.playerList.append(self)


	


class RedPlayer(Player):

	def __init__(self,name):
		Player.__init__(self.name)

	def walk(self):
		self.position = random.randint(1,10)
		

class BluePlayer(Player):

	def __init__(self,name):
		Player.__init__(self.name)

	def walk (self):
		self.position = random.randint(2,6)
		


red_start = int(input("How many red players do you want?"))
while True:
	if red_start == 0:
		break
	for i in range (1,red_start+1):
		red_name = input("Name for player " + str(i) + ": ")
		r = RedPlayer(red_name)
		r
		red_start-=1
			

blue_start = int(input("How many blue players do you want?"))	
while True:
	if blue_start == 0:
		break
	for i in range (1,blue_start+1):
		blue_name = input("Name for player " + str(i) + ": ")
		b = BluePlayer(blue_name)
		b
		blue_start-=1
	
	#Question 1
import random

class Player:
	playerList = []

	def __init__(self,name):
		self.name = name
		self.position = 0
		#self.playerList.append(self.name)
		#print(self.playerList)
		Player.playerList.append(self)


	


class RedPlayer(Player):

	def __init__(self,name):
		Player.__init__(self.name)

	def walk(self):
		self.position = random.randint(1,10)
		

class BluePlayer(Player):

	def __init__(self,name):
		Player.__init__(self.name)

	def walk (self):
		self.position = random.randint(2,6)
		


red_start = int(input("How many red players do you want?"))
while True:
	if red_start == 0:
		break
	for i in range (1,red_start+1):
		red_name = input("Name for player " + str(i) + ": ")
		r = RedPlayer(red_name)
		r
		red_start-=1
			

blue_start = int(input("How many blue players do you want?"))	
while True:
	if blue_start == 0:
		break
	for i in range (1,blue_start+1):
		blue_name = input("Name for player " + str(i) + ": ")
		b = BluePlayer(blue_name)
		b
		blue_start-=1
	
	


	class RedPlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def walk():
		print("walking")


class BluePlayer(Player):
	def __init__(self):
		Player.__init__(self)

	def walk():
		print("walking")