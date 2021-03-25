#kuisseuTatchim_edward_final_3.py
import requests
import xml.etree.ElementTree
import time

f = open("kuisseuTatchim_edward_latlon.txt","r")

new = open("tatchim_edward_latlon_clean.txt","w")

new_html = open("tatchim_edward.html","w")

new_js = open("tatchim_edward.js","w")

for i in f.readlines():
	raw = i.split(":")

	lat_raw = raw[1].split(",")
	lat_pure = lat_raw[0]
	#print(lat_raw)
	#print(lat_pure)

	long_raw = raw[2].split(",")
	long_raw2 = long_raw[0].split(" ")
	long_pure = long_raw2[1]

	ufo_raw = raw[3].split("\n")
	ufo_raw2 = ufo_raw[0].split(" ")
	ufo_pure = ufo_raw2[1]
	print(type(ufo_pure))

	ufo_lines =[lat_pure,long_pure,ufo_pure]
	#print(ufo_lines)
	new.write(ufo_lines)
	#print(lat_pure)
	#print(long_pure)
	#print(ufo_pure)


	#for z in raw:
	#	pure = z.split(",")
	#	print(pure)

	#break

f.close()
new.close()
new_html.close()
new_js.close()