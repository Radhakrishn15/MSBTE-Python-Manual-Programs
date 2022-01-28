String= 'Programming with Python'
lower= 0
upper = 0
for i in String:
 if(i.islower()):
  lower = lower+1
 elif(i.isupper()):
  upper = upper+1
print("Number of upper case letters:",upper)
print("Number of lower case latters:",lower)
"""Output
Number of upper case letters: 2
Number of lower case latters: 19

[Program finished]''""