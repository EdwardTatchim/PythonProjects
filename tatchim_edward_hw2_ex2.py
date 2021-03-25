import random
total = 0
enter = input("Hit enter to roll\n")

diceList1 = list()
numberOfRolls1 = 5

while numberOfRolls1!=0:
    dice1 = random.randint(1,6)
    diceList1.append(dice1)
    numberOfRolls1-=1
    
print(*diceList1,sep=",")

for i in diceList1:
    total = total + i
    
print("\nTotal score: " + str(total))

