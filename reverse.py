n=int(input("Enter Number:"))
rev =0
while (n>0):
	digit=n%10
	rev=rev*10+digit
	n=n//10
	print("Reverse Number:",rev)
	
"""	Output:
Enter Number:123
Reverse Number: 3
Reverse Number: 32
Reverse Number: 321

[Program finished]"""

"""n="123"[ : : -1]
print(n)

output
321

[Program finished]"""













