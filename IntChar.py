class IntChar:
	def same(self,n,c):
			if type(n)==int:
			   print ("Integer:",n)
			else:
				print ("Character:",n)
obj=IntChar()
obj.same(43,'Pranali') 
obj.same('Sakshi',41)#at the time of calling method overloading done


"""OUTPUT
Integer: 43
Character: Sakshi

[Program finished]"""