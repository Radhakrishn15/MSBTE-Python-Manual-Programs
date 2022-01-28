class Employee:
    def readInfo(self,name, department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        
    def printInfo(self):
        print("Name:", self.name,end="\n")
        print("Department:", self.department)
        print("Salary:", self.salary)

emp=Employee()
emp.readInfo("Sakshi",'IT',35000)
emp.printInfo()
	

"""OUTPUT

Name: Sakshi
Department: IT
Salary: 35000

[Program finished]" ""
    