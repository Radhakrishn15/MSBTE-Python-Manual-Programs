import operator
Dict={1:34,2:45,3:56,4:22,5:33,6:12}
print("Dictionary:",Dict)
sortedDict=dict(sorted( Dict.items(),key=operator.itemgetter(1)))
print("Ascending dictionary by value",sortedDict)
sortedDict=dict(sorted( Dict.items(),key=operator.itemgetter(1),reverse=True))
print("Descending dictionary by value",sortedDict)

"""output
Dictionary: {1: 34, 2: 45, 3: 56, 4: 22, 5: 33, 6: 12}
Ascending dictionary by value {6: 12, 4: 22, 5: 33, 1: 34, 2: 45, 3: 56}
Descending dictionary by value {3: 56, 2: 45, 1: 34, 5: 33, 4: 22, 6: 12}

[Program finished]"""

