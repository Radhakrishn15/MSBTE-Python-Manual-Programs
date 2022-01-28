class Invalidpassword(Exception):
    pass
def check(Password):
     Password="sakshi"
     if str(Password)==P :
        print(" Password is correct")
     else :
	      raise Invalidpassword

P = input("Ur password:")
check(P)

"""OUTPUT
Ur password:sak

  File "<string>", line 8, in check
__main__.Invalidpassword

#2nd time run

Ur password:sakshi
 Password is correct

[Program finished]



[Program finished]"""
