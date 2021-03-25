import random

class Player:
    playerList = []
    def __init__(self,name):
        #self.playerList = []
        self.name = name
        self.position = 0
        Player.playerList.append(name)
        print(name)

    
    def PlayerRoster(self):
        print(self.playerList)

    def walk(self):
        print("walking")
        
    def playing(self):
        for z in self.playerList:
            self.position = walk()
            print(self.position)

class RedPlayer(Player):
    def __init__(self,name):
        Player.__init__(self,name)
        #Player.playerList.append(name)
        self.position = 0

    def walk(self):
        self.walk()
        return random.randint(1,10)
    
class BluePlayer(Player):
    def __init__(self,name):
        Player.__init__(self,name)
        #Player.playerList.append(name)
        self.position = 0

    def walk(self):
        self.walk()
        return random.randint(2,6)
    
    def playing(self):
        self.position = 0
        self.Name = str()
        while self.position <= 100:
            for z in self.playerList:
                self.position += walk()
                self.Name = z
        print(self.Name + " is the winner with " + str(self.position) + " miles covered.")
    
    
red_start = int(input("How many red players do you want? "))

blue_start = int(input("How many blue players do you want? "))

while True:
    if red_start == 0:
        break
    for i in range (1,red_start+1):
        red_name = input("Name for red player " + str(i) + ": ")
        r = RedPlayer(red_name)
        #Player.playerList.append(r)
        #print(playerList[1])
        red_start-=1
r.PlayerRoster()        
        
while True:
    if blue_start == 0:
        break
    for i in range (1,blue_start+1):
        blue_name = input("Name for blue player " + str(i) + ": ")
        b = BluePlayer(blue_name)
        #b.playerList()
        #Player.playerList.append(b)
        #print(playerList[1])
        blue_start-=1
        

b.PlayerRoster()
b.playing()