import requests
import xml.etree.ElementTree

podcasts = requests.get("http://feeds.megaphone.fm/daily-inspiration")
root = xml.etree.ElementTree.fromstring(podcasts.content)
print(root)

#loop through tree root and return every line that contains item
for item in root.iter("item"):
	for attribute in item.iter("title"):
		#print("Tag: " + attribute.tag)
		print("Text: " + attribute.text)