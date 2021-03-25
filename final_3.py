import requests
import xml.etree.ElementTree
import time


new = open("latlon.txt","r")

new_html = open("golbeck_jen.html","w")

new_js = open("golbeck_jen.js","w")


lines = new.readlines()

for el in lines:
	line = el.split("\n")
	clean_1 = line[0]
	clean_2 = clean_1.split(",")
	lati = clean_2[0]
	longi = clean_2[1]
	ufo_count = clean_2[2]
	print(lati)
	print(longi)
	print(ufo_count)
	#print(clean_2)
	break
	#for element in line:
	#	clean = element.split(",")
	#	print(clean[0])
	#	print(clean[1])
	#	print(clean[2])
	#break
		#lati = clean[0]
		#longi = clean[1]
		#ufo_count = clean[2]
		#print(lati)
		#print(longi)
		#print(ufo_count)

#f.close()
new.close()
new_html.close()
new_js.close()