import requests
import xml.etree.ElementTree
import time
#myKey = '1quhVhyIFHboap7GkdtKijYe2mX3LMO7'
#loc = "Lethbridge (Canada)"
#url = "http://www.mapquestapi.com/geocoding/v1/address?outFormat=csv&key="+myKey+"&location="+loc
#results = requests.get(url)
#print(results.text)




#file extraction and dumping

f = open("tatchim_edward_cities.txt")
new_f = open("tatchim_edward_latlon_clean.txt","w")


#lat = str()
#Long = str()
#new_data = str()
#new_data_1 = str()

for i in f.readlines():
	city_raw = i.split("\n")
	city = city_raw[0].split("\t")

	#external com with the web
	location = city[0]
	ufo_count = city[1]
	myKey = 'sAS7KY1Zpv0KhB8NCtIJnpNWAxDaLPJ3'
	url = "http://www.mapquestapi.com/geocoding/v1/address?outFormat=csv&key="+myKey+"&location="+location
	results = requests.get(url)


	#internal processing of web data collected
	c=0
	for line in results.text.splitlines():
		if c==1:
			print("we'll extract")
			data = line.split(",")
			lat= data [6]
			lat = lat.replace('"','')
			Long= data [7]
			Long = Long.replace('"','')
		
		#print("Latitude :"+lat)
		#print("Longitude :"+Long)
			new_data_1 = ("City/State : %s, Latitude: %s, Longitude: %s, Count : %s\n"%(location, lat, Long, ufo_count))
		#print(new_data_1)
			new_data = ("%s,%s,%s\n"%(lat, Long, ufo_count))
			print(new_data_1)
			new_f.write(new_data)
			time.sleep(5)
		c = c+1
	#time.sleep(5)
	


f.close()
new_f.close()
