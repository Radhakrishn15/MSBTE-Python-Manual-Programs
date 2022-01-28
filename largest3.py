a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a >= b) and (a>= c):
   largest = a
elif (b>= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)

"""output
Enter first number: 8
Enter second number: 7
Enter third number: 6
The largest number is 8.0

[Program finished]"""