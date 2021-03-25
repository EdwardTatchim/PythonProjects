class Report:
	def __init__(self, animalID,name,animaltype,breed):
		self.id = animalID
		self.name = name
		self.type = animaltype
		self.breed = breed

class OutcomeReport(Report):
	def __init__(self,animalID,name,animaltype,breed,outcome):
		Report.__init__(self,animalID,name,animaltype,breed)
		self.outcome = outcome

class IntakeReport(Report):
	def __init__(self,animalID,name,animaltype,breed,outcome,intakeType,condition):
		Report.__init__(self,animalID,name,animaltype,breed)
		self.intakeType = intakeType
		self.condition = condition



intakeReports = []
f = open("intakes.csv")
while True:
	line = f.readline()
	if (len(line)==0):
		break
	data = line.split(",")
	r = IntakeReport(data[0],data[1],data[7], data[10],data[5],data[6],data[2])
	intakeReports.append(r)
print(intakeReports)	
f.close




outcomeReports = []
f = open("outcomes.csv")
while True:
	line = f.readline()
	if (len(line)==0):
		break
	data = line.split(",")
	r = outcomeReport(data[0],data[1],data[7], data[10],data[5],data[6],data[2])
	outcomeReports.append(r)
print(outcomeReports)	
f.close