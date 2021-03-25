
class Robot:
	def __init__ (self, name):
		self.myName = name
		print("Creating new robot.")
	
c3p0 = Robot("C-3PO")
print (c3p0.myName)