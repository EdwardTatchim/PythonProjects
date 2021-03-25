import random
keyboard2=input("Hit enter to roll\n")
print("You rolled\n")
times = 4

spinList=list()
spinList2=list()
while times!=0:
    spin = random.randint(1,6)
    spinList.append(spin)
    times-=1
    
print(*spinList, sep=",")


spinList2=spinList2+spinList
#print(spinList2)
win = 0
winList=list()
ind = int()
#occurence=list()
for i in spinList:
    if i in spinList2:
        ind = spinList2.count(i)
        #print(ind)
        if ind >= 2:
            win = 2
        winList.append(win)
        
#print(winList)
    #occurence[i]=spinList2.count(i)
        
        
if win>=2:
    print("\nYOU WIN!")
else:
    print("\nYou Lose")
    
    