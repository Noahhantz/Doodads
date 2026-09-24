'''
Simple triangle side calculator using a^2 + b^2 = c^2.
input the two side lengths that you want to test and use the proper formula (instructions below in green coments.)
if you only have one side value and two unknown lengths...above my paygrade
'''
#select two values and set two of the three sides to one of those two variables
#set the remaining side equal to " "

side1 = " " 
side1_given = side1
side2 = " "
side2_given = side2
side3 = " "
side3_given = side3

if (side1_given == " " and side2_given == " ") or (side1_given == " " and side3_given == " ") or (side2_given == " " and side3_given == " ") or (side1_given == " " and side2_given == " " and side3_given == " "):
    print("Insufficient data acquired, cannot compute.")
    exit()

if side1 == " ":
    side1 = (side2 ** 2 / side3 ** 2) ** (1 / 2)
if side2 == " ":
    side2 = (side1 ** 2 / side3 ** 2) ** (1 / 2)
if side3 == " ":
    side3 = (side1 ** 2 + side2 ** 2) ** (1 / 2)


if side1_given != " " and side2_given != " ":
    print("If side one = " + str(side1) + " and side two = " + str(side2) + ", then side three = " + str(side3))
if side1_given != " " and side3_given != " ":
    print("If side one = " + str(side1) + " and side three = " + str(side3) + ", then side two = " + str(side2))
if side2_given != " " and side3_given != " ":
    print("If side two = " + str(side2) + " and side three = " + str(side3) + ", then side one = " + str(side1))
    

 