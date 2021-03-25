import random


class Player:

	def __init__(self,name):
		self.name = name
		self.position = 0
		self.playerList = []
		self.playerList.append(name)

		#self.red_start = int(input("How many red players do you want? "))
		#self.blue_start = int(input("How many blue players do you want? "))
	

class RedPlayer(Player):
	#self.red_start = int(input("How many red players do you want? "))
	def __init__(self,name):
		Player.__init__(self,name)
		#self.playerList.append(name)
		self.rname = str()
		self.position1 = 0
		
	def play(self):
		for w in self.playerList:
			while self.position1 < 100:
				#print(w + " is walking")
				self.position1 += self.walk()
				self.rname = w
		print("\nnRedPlayer winner is " + self.rname + " with distance covered " +str(self.position1)+ " miles.\n")

		


	def walk(self):
		self.position = random.randint(1,10)
		return self.position


class BluePlayer(Player):
	#self.blue_start = int(input("How many blue players do you want? "))
	def __init__(self,name):
		Player.__init__(self,name)
		#self.playerList.append(name)
		self.bname = str()
		self.position2 = 0
		
		
	def walk(self):
		self.position = random.randint(2,6)
		return self.position

	def play(self):
		for z in self.playerList:
			while self.position2 < 100:
				#print(z + " is walking")
				self.position2 += self.walk()
				self.bname = z
		print("\nBluePlayer winner is " + self.bname + " with distance covered " +str(self.position2)+ " miles.")
				



red_start = int(input("How many red players do you want? "))

while True:
			if red_start == 0:
				break
			for i in range (1,red_start+1):
				red_name = input("Name for red player " + str(i) + ": ")
				#self.playerList.append(self.red_name)
				r = RedPlayer(red_name)
				#Player.playerList.append(r)
				#print(playerList[1])
				red_start-=1

#r.playerList()


blue_start = int(input("How many blue players do you want? "))

while True:
			if blue_start == 0:
				break
			for i in range (1,blue_start+1):
				blue_name = input("Name for blue player " + str(i) + ": ")
				b = BluePlayer(blue_name)
				#Player.playerList.append(b)
				#print(playerList[1])
				blue_start-=1


r.play()
b.play()

