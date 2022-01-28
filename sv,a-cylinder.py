PI = 3.14
radius = float(input("Enter the Radius of a Cylinder: "))
height = float(input("Enter the Height of a Cylinder: "))
Surface_Volume = PI * radius * radius * height
Area = 2 * PI * radius * (radius + height)
print("\nThe Surface Volume of a Cylinder = %.2f" %Surface_Volume)
print("\nThe area of a Cylinder = %.2f" %Area)

"""output
Enter the Radius of a Cylinder: 9
Enter the Height of a Cylinder: 7

The Surface Volume of a Cylinder = 1780.38

The area of a Cylinder = 904.32

[Program finished]"""
