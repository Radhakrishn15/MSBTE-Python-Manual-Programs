class Degree:
   def getDegree (self):
   	print ("I got a degree")

class Undergraduate (Degree) :
	def getDegree (self):
		print("I am an undergraduate")

class Postgraduate (Degree) : 
     def getDegree(self):
     	print("I am a Postgraduate" )
obj1=Degree()
obj1.getDegree()
obj2=Undergraduate()
obj2.getDegree ()
obj3=Postgraduate ()
obj3.getDegree ()

OUTPUT
I got a degree
I am an undergraduate
I am a Postgraduate

[Program finished]