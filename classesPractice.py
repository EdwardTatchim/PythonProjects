#building a dice game
#dice game with some number of players. 
#each player rolls a die and the highest die wins
import random

class Game:
    def __init__(self):
        self.playerList = []
        self.WinningPlayerNumber = 0
        self.numberOfPlayers = int(input("How many players?"))
        for i in range (1,self.numberOfPlayers+1):
            self.playerList.append(Player(i))
        self.playGame()


    def playGame(self):
        playerNum = 0
        for player in self.playerList:
            input(player.name + ", it's your turn. Hit enter to roll.")
            player.score = self.rollDie()
            print(player.name + " rolled " + str(player.score))
            #track the winner
            if(player.score > self.playerList[self.WinningPlayerNumber].score):
                self.WinningPlayerNumber = playerNum
                print(player.name + " is the current winner. " )
            playerNum = playerNum + 1

        print(self.playerList[self.WinningPlayerNumber].name, "wins")

    def rollDie(self):
        return random.randint(1,6)
        

class Player:
    def __init__(self, number):
        self.name = input("Enter your name " + str(number) + ":" )
        #picked -1 bcse it is lower than any value rolled
        #on a die. Makes sure player actually rolls a die
        self.score = -1 
        
        
g = Game()