import requests
from bs4 import BeautifulSoup
import time


class StationData:
	def __init__(self,StationIn,EntriesIn,ExitsIn):
		self.station = StationIn
		self.entries = EntriesIn
		self.exits = ExitsIn

page = requests.get("http://web.mta.info/developers/turnstile.html")
soup = BeautifulSoup(page.text, "html.parser")
links = soup.findAll("a")

#print(page)
#print(soup)
#print(links)
#print(links)
i=255
while i<256:#len(links):
	url = "http://web.mta.info/developers/" + links[i]["href"]
	print (url)
	data = requests.get(url)
	for line in data.text.splitlines():
		info = line.split(",")
		print (url)
		print (info[3])
		print (info[9])
		print (info[10])

	time.sleep(1)
	i = i+1
#handle the data