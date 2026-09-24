'''
Simple triangle side calculator using a^2 + b^2 = c^2.
input the two side lengths that you want to test and use the proper formula (instructions below in green coments.)
if you only have one side value and two unknown lengths...above my paygrade
'''

#Formula for side1; set side1 equal to this: (side2 ** 2 / side3 ** 2) ** (1 / 2)
#Formula for side2; set side2 equal to this: (side1 ** 2 / side3 ** 2) ** (1 / 2)
#formula for hypotenuse; set side3 equal to this: (side1 ** 2 + side2 ** 2) ** (1 / 2)

side1 = 1
side2 = 2
side3 = (side1 ** 2 + side2 ** 2) ** (1 / 2)

print("Side 1: " + str(side1) + "\nSide 2: " + str(side2) + "\nSide 3/hypotenuse: " + str(side3))

