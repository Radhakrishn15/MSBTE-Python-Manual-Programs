a={0,2,4,6,8}
b={1,2,3,4,5}
print("Intersection of sets",a|b)
print("Union of sets",a&b)
print("Set difference",a-b)
print("Symmentric difference",a^b)
print("clear a set",a.clear())
print (a)
print(b)


"""output
Intersection of sets {0, 1, 2, 3, 4, 5, 6, 8}
Union of sets {2, 4}
Set difference {0, 8, 6}
Symmentric difference {0, 1, 3, 5, 6, 8}
clear a set None
set()
{1, 2, 3, 4, 5}

[Program finished]"""
