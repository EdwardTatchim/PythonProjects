#question 2 and 3
class WeatherObservation:

    def __init__(self,date, temp, pressure,humidity,windspeed):
        
        #question 6
        self.mygroup = []
        
        self.mydate = date
        self.mygroup.append(self.mydate)
        
        self.mytemp = temp
        self.mygroup.append(self.mytemp)
        
        self.mypressure = pressure
        self.mygroup.append(self.mypressure)
        
        self.myhumidity = humidity
        self.mygroup.append(self.myhumidity)
        
        self.mywindspeed =  windspeed
        self.mygroup.append(self.mywindspeed)
        
        #print(self.d)
        
        #self.mygroup = [self.mydate, self.mytemp,self.mypressure,self.myhumidity,self.mywindspeed]
        #print(self.mygroup)

#question 4
    def printObservation(self):
        print(self.mydate)
        print(self.mytemp)
        print(self.mypressure)
        print(self.myhumidity)
        print(self.mywindspeed)


#question 1

f = open('weather.txt','r')
line = f.readlines()
line = line[1:]
#print(line)

f.close()

while True:
    if (len(line)==0):
        break
    temp_avg=0
    temp_sum = 0
    
    pressure_avg=0
    pressure_sum = 0
    
    hum_avg=0
    hum_sum = 0
    
    windsp_avg=0
    windsp_sum = 0
    
    temp_list = []
    
    press_list =[]
    
    hum_list =[]
    
    windsp_list =[]
    
    
    for i in line:
        weatherClean = i.split("\t")
        weatherClean_2 = [x.replace('\n', '') for x in weatherClean]
        #print("Date :" + weatherClean_2[0] + "Temperature: " + str(weatherClean_2[1]))

#question 5
        observation1 = WeatherObservation(weatherClean_2[0],weatherClean_2[1],weatherClean_2[2],weatherClean_2[3],weatherClean_2[4])
        #observation1.printObservation()
        #print("Printing new observation")
        #line_1 = observation1.printObservation()
        #observation1.d
        #for z in observation1.mygroup:
            #print(observation1.mygroup[0],observation1.mygroup[1],observation1.mygroup[2],observation1.mygroup[3],observation1.mygroup[4])
            
        
#question 7
        #for b in observation1.mygroup:
        t = observation1.mygroup[1]
        temp_list.append(float(t))
            
        p = observation1.mygroup[2]
        press_list.append(float(p))
            
        h = observation1.mygroup[3]
        hum_list.append(int(h))
            
        w = observation1.mygroup[4]
        windsp_list.append(int(w))
        #print(temp_list)
        
        
    for d in temp_list:
        temp_sum += d
        temp_avg = temp_sum/len(temp_list)
        #print(temp_sum)
    for e in press_list:
        pressure_sum += e
        pressure_avg = pressure_sum/len(press_list)
    for f in hum_list:
        hum_sum = hum_sum + f
        hum_avg = hum_sum/len(hum_list)
    for g in windsp_list:
        windsp_sum = windsp_sum + g
        windsp_avg = windsp_sum/len(windsp_list)
        
    print("Avg Temperature: " + str(round(temp_avg,4)))
    print("Avg Pressure: " + str(round(pressure_avg,4)))
    print("Avg Humidity: " + str(round(hum_avg,4)))
    print("Avg WindSpeed: " + str(round(windsp_avg,4)))
    break
            
        