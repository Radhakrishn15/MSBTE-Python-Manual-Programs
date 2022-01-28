def upperlower(s):
    uppercase=0
    lowercase=0
    for c in s:
        if c.isupper():
           uppercase+=1
        elif c.islower():
           lowercase+=1
        else:
           pass
    print ("Number of Upper case letters: ", uppercase)
    print ("Number of Lower case letters: ", lowercase)
upperlower('Programming with Python')

"""Output
Number of Upper case letters:  2
Number of Lower case letters:  19

[Program finished]"""
