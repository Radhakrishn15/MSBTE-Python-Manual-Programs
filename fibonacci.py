n1=0
n2=1
counter=0
n=int (input("enter number"))#n=5
if n>=0:
  while counter<=n:
  	print(n1)
  	temp=n1+n2
  	n1=n2
  	n2=temp
  	counter=counter+1
  	
 """output
 enter number5
0
1
1
2
3
5

[Program finished]"""