red_start = int(input("How many red players do you want?"))
while True:
	if red_start == 0:
		break
	for i in range (1,red_start+1):


blue_start = int(input("How many blue players do you want?"))



def walker(cls):
		first_place_winner = False
		while True:
			for playa in Player.playerList:
				playa.walk()
				print(playa.name + ' walked' + str(playa.position) + ' miles.')
				if playa.self.position>=100:
					print(playa.name + " is the first_place_winner")
					first_place_winner = True
					break
			print()
			if first_place_winner == True:
				break

def mainScript():
	Player.walker(Player)


mainScript()