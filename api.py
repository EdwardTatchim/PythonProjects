import requests
import xml.etree.ElementTree

zip = input("Enter zipcode to get sun rise and sun set times :   ")
appId = "ead0b99ec9e326d2d933143bf2c6e75f"
#pulling our request from the API
data = requests.get("http://api.openweathermap.org/data/2.5/forecast?mode=xml&zip=" +zip+",us&APPID="+appId)
#print(data.text)

#taking text and asking xml element tree package
#to process that string of xml
#variable root is the root of the tree that we want to access
root = xml.etree.ElementTree.fromstring(data.text)
for sunData in root.iter("sun"):

	sunRise = sunData.attrib["rise"]
	sunRiseParts = sunRise.split("T")
	sunRiseTime = sunRiseParts [1]

	sunSet = sunData.attrib["set"]
	sunSetParts = sunSet.split("T")
	sunSetTime = sunSetParts [1]

	print("Sun rise is at " + sunRiseTime)
	print("Sun set is at " + sunSetTime)
	
#print(root)