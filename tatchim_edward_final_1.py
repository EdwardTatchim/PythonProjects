import requests
from bs4 import BeautifulSoup
import urllib.request
import time
#import xml.etree.ElementTree
import feedparser

url = "http://www.cs.umd.edu/~golbeck/INST326/ndxe201902.html"
ufo = requests.get(url)
ufo_content = ufo.text
ufo_soup = BeautifulSoup(ufo_content, "html.parser")
#print(ufo_soup)

city = []
state = []
for element in ufo_soup.find_all('tr'):
	tag = element.find_all('td')
	for mem in tag:
		precision = mem.find_all(' ')
	#city.append(tag[1].text)
	#state.append(tag[2].text)
#print("Date/Time : %s, City : %s, State :%s, Shape : %s, Duration : %s, Summary : %s, Posted : %s\n "% 
		#(tag[0].text,tag[1].text,tag[2].text,tag[3].text,tag[4].text,tag[5].text,tag[6].text))



#print(ufo_soup)
#city = []
#state = []
#complete_file = dict()
#for trs in ufo_soup.findall('tr'):
	#tag = trs.findall('td')
	#print("Date/Time : %s, City : %s, State :%s, Shape : %s, Duration : %s, Summary : %s, Posted : %s\n "% 
		#(tag[0].text,tag[1].text,tag[2].text,tag[3].text,tag[4].text,tag[5].text,tag[6].text))

#	time.sleep(5)
	#city.append(tag[1].text)
	#state.append(tag[2].text)

#for i in city:
	#occur = 0
	#occur = count(i)
	#complete_file [i] = occur

#print(complete_file)

#link = tag.text['href']
#print(tag)
#print(link)
	#time.sleep(5)