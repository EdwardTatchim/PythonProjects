import pickle
#f=open("testOut.txt","w")
#f.write("today is great!")
#f.close()


f = open("sp.csv") #opens a file
fOut = open ("spAvg.txt","wb")
while True:
	line = f.readline()   #reads the next line
	if (len(line) == 0):
		break
	months = line.split(",") #breaks up a string ","
	year = months[0];
	m2 = months[1:len(months)-1]  #sublist
	m2 = [float(x) for x in m2]   #casts/changes type of all elements in the list
	pickle.dump(m2,fOut)
	#average = sum(m2)/len(m2)
	#fOut.write(year + ": "+ str(average) + "\n")
f.close()
fOut.close()




