word=('zero','one','two','three','four','five','six','seven','eight','nine')
number=input("Enter number: ") 
n=[]
for a in number:
    n.append(word[int(a)])
    print (n)
    
"""'output
Enter number: 5
['five']

[Program finished]"""

