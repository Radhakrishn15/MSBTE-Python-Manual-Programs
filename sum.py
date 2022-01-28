n=int(input("Enter Number:"))
sum =0
while (n>0):
	digit=n%10
	sum=sum +digit
	n=n//10
	print("sum of digits in number:",sum)
	
"""	Output
Enter Number:123
sum of digits in number: 3
sum of digits in number: 5
sum of digits in number: 6

[Program finished]"":