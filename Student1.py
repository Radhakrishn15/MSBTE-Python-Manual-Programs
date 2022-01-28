class Student:
	def __init__(self, Name, Age):
		self.Name = Name
		self.Age = Age

class Teacher (Student):
	def ShowData(self):
		print("Name=",self.Name)
		print("Age=",self.Age)
		
obj= Teacher("Sakshi",18)
obj.ShowData() 

''''Output

Name= Sakshi
Age= 18

[Program finished]"""