color=set()
color.add("Red")
print("Add member:",color)
color.update(["Blue","Violet"])
print("Add members:",color)
color.remove("Blue")
print("After removing blue color set is ",color)

"""output
Add member: {'Red'}
Add members: {'Blue', 'Violet', 'Red'}
After removing blue color set is  {'Violet', 'Red'}

[Program finished]"""