import math #adding library for aritmetcal calculations
print("Let's calculate the area of a triangle \n Please add below the lengths of each side of your triangle")
side1 = float(input("Add L1: "))
side2 = float(input("Add L2: "))
side3 = float(input("Add L3: "))
s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(f"The area of your triangle is: {area}")

