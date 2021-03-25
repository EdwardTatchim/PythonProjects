import pickle

f = open("UFO_data.txt")
new_f = open("Tatchim_Edward_cities.txt", "wb")
while True:
	for i in f.readlines():
		#city/state = 
		city_raw = i.split("\n")
		city = city_raw[0].split("\t")
		location = city[0]
		ufo_count = city[1]
		print(ufo_count)
		break
	break





	#city_and_info = f_line.split(",")
	#for i in city_and_info:
	#	city = i.split("\t")
	#	print(city[0])
	#break
	#print(city)
	#f2
	#pickle.dump(f2,new_f)
	
	