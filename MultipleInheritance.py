class Father:
	def msg(self):
		print("This is Father class")  

class Mother:
	def msg(self):
		print("This is a Mother class")
		
class Child(Father,Mother):
	def msg(self):
		print("This is a Child class")   

f = Father() 
f.msg()
m=Mother ()
m.msg()
c=Child()
c.msg()


"""OUTPUT
This is Father class
This is a Mother class
This is a Child class

[Program finished] """