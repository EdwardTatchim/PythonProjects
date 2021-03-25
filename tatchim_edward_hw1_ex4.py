import random
dieList = (0.1,0.2,0.2,0.2,0.2,0.1)

def rollDie(dieChances):
    ranRoll = random.random() # roll between 0 and 1
    sum=0
    result = 1
    for chance in dieChances:
        sum += chance
        if ranRoll < sum:
            return result
        result +=1
        
print(rollDie(dieList))