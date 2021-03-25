import random
#checking for 6,5,4 and saving their occurence
def check(m):
    six=0
    five=0
    four=0
    for n in m:
        if n == 6:
            six=six+1
        elif n == 5:
            five=five+1
        elif n ==4:
            four=four+1
        #else:
            #print("No captain, ship, or crew")
    #print(str(six),str(five),str(four))
    return six,five,four
            
def rollDie():
    '''This is a special type of comment'''
    die = random.randint(1,6)
    #print("You rolled " + str(die))
    return die

def shipCaptainCrew():
    #print("Running playWithIteration-" + str(n))
    #know when to stop
    #nA=6
    
    currentMax = 0
    rounds=3
    chancesArray1 = []
    chancesArray2 = []
    chancesArray3 = []
    winnerList = []
    ship = []
    expectation = [6,5,4]
    for i in range (1,rounds+1):
        if(i==rounds+1):
            print("\t n is 0 so we stop and return 0 ")
            return 0
        
        #Round 1
        if i == 1:
            print ("round "+ str(i))
            numberOfDice = 5
            while numberOfDice!=0:
                r = rollDie()
                chancesArray1.append(r)
                numberOfDice-=1   
            print(*chancesArray1,sep=",")
            sixth = check(chancesArray1)
            
            if sixth[0]==0:
                print("continuing to round 2")
            else:
                sixx = expectation.pop(0)
                winnerList.append(sixx)
                if sixth[1]==0:
                    print("Continuing to round 2")
                else:
                    fivv = expectation.pop(0)
                    winnerList.append(fivv)
                    if sixth[2]==0:
                        print("Continuing to round 2")
                    else:
                        fourr = expectation.pop(0)
                        winnerList.append(fourr)
   
            print(sixth)
            print("winnerlist",winnerList)
            
            
        
        #Round 2    
        elif i == 2:
            print ("round "+ str(i))
            if '6' in winnerList:
                numberOfDice = 4
            elif '5' in winnerList:
                numberOfDice = 3
            elif '4' in winnerList:
                    numberOfDice = 2
            else:
                numberOfDice = 5
            while numberOfDice!=0:
                r = rollDie()
                chancesArray2.append(r)
                numberOfDice-=1
            print(*chancesArray2,sep=",")
            fifth = check(chancesArray2)
            print(fifth)
            if fifth[0]==0:
                print("continuing to round 2")
            else:
                sixx = expectation.pop(0)
                winnerList.append(sixx)
                if sixth[1]==0:
                    print("Continuing to round 2")
                else:
                    fivv = expectation.pop(0)
                    winnerList.append(fivv)
                    if sixth[2]==0:
                        print("Continuing to round 2")
                    else:
                        fourr = expectation.pop(0)
                        winnerList.append(fourr)
            print("winnerlist",winnerList)
            
        #Round 3    
        elif i == 3:
            print ("round "+ str(i))
            numberOfDice = 5
            while numberOfDice!=0:
                r = rollDie()
                chancesArray3.append(r)
                numberOfDice-=1
            print(*chancesArray3,sep=",")
            fourth = check(chancesArray3)
            print(fourth)
            if(fourth[0]<=0):
                continue
            elif(fourth[0]>0):
                chancesArray3.remove(6)
                if 6 not in winnerList:
                    winnerList.append(6)
            if(fourth[1]<=0):
                continue
            elif(fourth[1]>0):
                chancesArray3.remove(5)
                if 5 not in winnerList:
                    winnerList.append(5)
            if(fourth[2]<=0):
                continue
            elif(fourth[2]>0):
                chancesArray3.remove(4)
                if 4 not in winnerList:
                    winnerList.append(4)
            print(*chancesArray3,sep=",")
            print(winnerList)
            
        else:
            print("You have exhausted all your chances to succeed")

    

    
    #print("\t The max on round " + str(n) + " is " + str(currentMax))
    #add to total
    #print("\t Now calling playWithIteration of " + str(n-1))
    #return currentMax + playWithIteration(n-1)

#total=0
#total = playWithIteration(3)
#print("The total is " + str(total))

shipCaptainCrew()