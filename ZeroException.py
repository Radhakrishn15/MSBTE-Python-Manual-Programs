try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b;    
except ZeroDivisionError as e:
    print("Divide by zero Exception",e) 
else:
	 print(" Result:",a/b) 
    
"""Output
Enter a:6
Enter b:0
Divide by zero Exception 

#2nd time run
Enter a:6
Enter b:2
 Result: 3.0

[Program finished]


[Program finished]

[Program finished]"""