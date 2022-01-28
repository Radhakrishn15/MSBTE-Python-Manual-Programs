from collections import Counter
dict={'a':56,'b':66,'c':77,'d':88,'e':99,'f':100}
k = Counter(dict) 
high = k.most_common(3)  
print("Initial Dictionary:") 
print(dict, "\n") 
print("Dictionary with 3 highest values:") 
print("Keys: Values") 
for i in high: 
  print(i[0]," :",i[1]," ")
 
 
"""output
Initial Dictionary:
{'a': 56, 'b': 66, 'c': 77, 'd': 88, 'e': 99, 'f': 100}

Dictionary with 3 highest values:
Keys: Values
f  : 100
e  : 99
d  : 88

[Program finished]"""
    
    
    
    
