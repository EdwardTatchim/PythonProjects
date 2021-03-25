
class Robot:
	numberOfRobots=0

	def __init__ (self, name):
		self.myName = name
		print("Creating new robot.")
		Robot.numberOfRobots = Robot.numberOfRobots+1
		
	def sayHello(self):
		print ("Hello from " + self.myName)
	
c3p0 = Robot("C-3PO")
print (c3p0.myName)
print (c3p0.numberOfRobots)
c3p0.sayHello()

r2d2 = Robot("R2")
r2d2.sayHello()
print (c3p0.numberOfRobots)
print (r2d2.numberOfRobots)

