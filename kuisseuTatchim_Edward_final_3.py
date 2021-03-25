#kuisseuTatchim_edward_final_3.py
import requests
import json
import time


f = open("kuisseuTatchim_edward_latlon.txt")
new = open("tatchim_edward_latlon_1.txt")

new_html = open("tatchim_edward.html","w")

new_js = open("tatchim_edward.js","w")

#key = 'QC7WTFIp8i1sIkMKucl2y5gaawWponXZ'
#url = "https://developer.mapquest.com/documentation/mapquest-js/v1.0/examples/showing-clusters-as-a-heat-map/"
#results = requests.get(url)
#soup = BeautifulSoup(results.text, "html.parser")
#link =  soup.findall("a")

#print(soup.find(script))
#root = xml.etree.ElementTree.fromstring(results.text)
#print(root)


#for line in results.text.splitlines():
#	data = line.split(",")

#	print(data)

coord = "var addressPoints=["
in_file = open("tatchim_edward_latlon_1.txt")

with in_file:
    next(in_file)
    for member in in_file:


    	#print(member)
    	#break
        line=member.split(",")
        
        laty = line[0]
        longy = line[1]
        ufy = line[2]

        coord = ("%s\n[%s,%s,'%s']," %(coord, laty, longy, ufy))

coord = coord.strip(",")
coord = coord+"];"

new_js.write(coord)

mapquest_html = ('''<html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src="tatchim_edward.js"></script>

    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'QC7WTFIp8i1sIkMKucl2y5gaawWponXZ';
        var baseLayer = L.mapquest.tileLayer('map');

        var map = L.mapquest.map('map', {
          center: [39.80, -98.50],
          layers: baseLayer,
          zoom: 7
        });

        addressPoints = addressPoints.map(function (addressPoint) { return [addressPoint[0], addressPoint[1]]; });
        
        L.heatLayer(addressPoints).addTo(map);
      }
    </script>
  </head>

  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>
        
        
        ''')


new_html.write(mapquest_html)
#for i in new.readlines():
#	line = i.split(",")
#	lat = line[0]
#	lon = line[1]
#	ufo = line[2]
	#print(line[1])
	#print(line[2])
#	break
	
#\	see = i.split(",")
#	laty = see[0].replace('Lat: ','')
#	longy = see[1].replace(' Long: ','')
#	ufy = see[2].replace(' UFO count : ','')
#	print(laty)
#	print(longy)
#	print(ufy)
#	ufo_line =laty+","+longy+","+ufy
#	print(ufo_line)
#	new.write(ufo_line)
	#break

f.close()
new.close()
new_html.close()
new_js.close()