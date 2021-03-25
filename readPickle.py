import pickle
f = open("spAvg.txt","rb")

while True:
	#do stuff
	try:
		m = pickle.load(f)
		print(sum(m)/len(m))
	except EOFError:
		break
		
f.close()