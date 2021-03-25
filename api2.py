import requests
import xml.etree.ElementTree

myKey = 'QC7WTFIp8i1sIkMKucl2y5gaawWponXZ'
loc = "Keaton Beach,FL"
url = "http://www.mapquestapi.com/geocoding/v1/address?outFormat=csv&key="+myKey+"&location="+loc
results = requests.get(url)
#print(results.text)

#lat = str()
#Long = str()
c=0
for line in results.text.splitlines():
	if c==1:
		print("we'll extract")
		data = line.split(",")
		print(data)
		lat= data [6]
		lat = lat.replace('"','')
		Long= data [7]
		Long = Long.replace('"','')
	c=c+1

print("Latitude :"+lat)
print("Longitude :"+Long)

#root = xml.etree.ElementTree.fromstring(results.text)
#for attribute in root:
#	print(attribute)
