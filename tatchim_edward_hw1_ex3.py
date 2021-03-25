import random
numberOfSides = int(input("How many sides should the die have? "))
numberOfDice = int(input("How many dice should be rolled? "))
chancesArray = []
while numberOfDice!=0:
    diceRoll = random.randint(1,numberOfSides)
    chancesArray.append(diceRoll)
    numberOfDice-=1
print(chancesArray)