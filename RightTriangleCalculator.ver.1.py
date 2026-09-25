side1 = 1
side1_given = side1
side2 = 19
side2_given = side2
side3 = 10
side3_given = side3

angle3 = 90
#this calculator is intended for right triangles only. Changing the value of angle3 will not function and an error will be returned.

if ((side1 != "" and side2 == "" and side3 == "") or (side1 == "" and side2 != "" and side3 == "") or (side1 == "" and side2 == "" and side3 != "") or (side1 == "" and side2 == "" and side3 == "")):
    print("Error: Insufficient Data acquired for calculation. Please define two sides.")
    exit()
if (side1 != "" and side2 != "" and side3 != ""):
    print("Error: Three sides defined. Please only define two sides.")
    exit()
if (angle3 != 90):
    print("Error: non-right angle detected, consult code. Insure 'angle3 = 90'.")
    exit()
if ((side1 != "" and side1 <= 0) or (side2 != "" and side2 <= 0) or (side3 != "" and side3 <= 0)):
    print("Error: Invalid side(s); must be greater than 0")
    exit()
if ((side3 != "" and side1 != "" and side3 <= side1) or (side3 != "" and side2 != "" and side3 <= side2)):
    print("Error: Hypotenuse must be the longest side in a right triangle.\nEnsure side3 > side1 and side2 or is undefined.")
    exit()
    
import math
    
if side1 == "":
    side1 = math.sqrt(side3 ** 2 - side2 ** 2)
if side2 == "":
    side2 = math.sqrt(side3 ** 2 - side1 ** 2)
if side3 == "":
    side3 = math.sqrt(side1 ** 2 + side2 ** 2)
    
if side2_given != "" and side3_given != "":
    angle1 = math.degrees(math.asin(side2 / side3)) 
if side1_given != "" and side3_given != "":
    angle1 = math.degrees(math.acos(side1 / side3)) 
if side1_given != "" and side2_given != "":
    angle1 = math.degrees(math.atan(side2 / side1)) 
    
if side1_given != "" and side3_given != "":
    angle2 = math.degrees(math.asin(side1 / side3)) 
if side2_given != "" and side3_given != "":
    angle2 = math.degrees(math.acos(side2 / side3)) 
if side1_given != "" and side2_given != "":
    angle2 = math.degrees(math.atan(side1 / side2)) 
    
if (angle1 + angle2 + angle3) != 180:
    print("Error: Angles do not sum to 180 degrees; not a triangle")
    exit()
    #I do not think this is a possible error to achieve given previous checks.
    #unless you input three random values for all three sides then maybe.
    #If by any means you see this message, either the computer did math wrong (if so rerun the code)
    #or there is a bug in the code. If so please contact me.
    
area = (1 / 2) * (side1 * side2)
    
print("Side 1 = " + str(side1) + ": Side 2 = " + str(side2) + ": Side 3/Hypotenuse = " + str(side3))
print("Angle 1 = " + str(angle1) + ": Angle 2 = " + str(angle2) + ": Angle 3 = " + str(angle3))
print("Area = " + str(area))

