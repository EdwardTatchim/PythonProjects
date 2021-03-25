import random

key = input("Hit enter to roll")
print("\nYou rolled\n")
dieNumbers=(1,2,3,4,5)
dieLists=list()

for i in dieNumbers:
    rolling = random.randint(1,6)
    print("Die" , str(i),":",str(rolling),"\n")
    dieLists.append(rolling)
#print(dieLists)    
keyboard = int(input("Which die would you like to keep? "))
print("\nYou saved die "+str(keyboard)+" with a value of "+str(dieLists[keyboard-1])+"\n")

enter1 = input("Hit enter to roll the remaining dice\n")
print("You rolled \n")
savedDie = dieLists.pop(keyboard-1)
#print("saved die "+str(savedDie))

dieNumbers1 =(1,2,3,4)
dieLists2=list()
for i in dieNumbers1:
    rolling2 = random.randint(1,6)
    print("Die" , str(i),":",str(rolling2),"\n")
    dieLists2.append(rolling2)
#print(dieLists2)

totalScore = 0

for i in dieLists2:
    totalScore +=i

#print(dieLists2)
#print("Total score "+str(totalScore))
print("\nYour total score is "+ str(totalScore+savedDie))