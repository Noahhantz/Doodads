#simple triangle side calculator, using a^2 + b^2 = c^2
#select two values and set two of the three sides to one of those two variables
#set the remaining side equal to ""
#note side3 is always the hypotenuse, the other two sides can be interchanged
#if more than one side is set equal to "", an error will be returned
'''
added area, angle and height calculation. Change the value of var.angle1 to test different triangles:
note that side1 is always the angle adjacent to the hypotenuse, the other two angles can be interchanged
'''

side1 = ""
side1_given = side1
side2 = 4
side2_given = side2
side3 = 5
side3_given = side3
angle1 = 89
angle1_given = angle1
angle2 = 45
angle2_given = angle2
angle3 = ""
angle3_given = angle3

if (angle1 == 90 or angle2 == 90 or angle3 == 90) and (side3 != "" and (side1 != "" and side3 <= side1) or (side2 != "" and side3 <= side2)):
    print("Hypotenuse at impossible length: too short. Triangle destroyed.")
    exit()
if (side1_given == "" and side2_given == "") or (side1_given == "" and side3_given == "") or (side2_given == ""  and side3_given == "") or (side1_given == "" and side2_given == "" and side3_given == ""):
    print("Insufficient data acquired, cannot compute.")
    exit()
if(side1_given != "" and (side1_given <= 0) or side2_given != "" and (side2_given <= 0) or side3_given != "" and (side3_given <= 0)):
    print("missing side(s), triangle destroyed.")
    exit()
if (angle1_given == "" and angle2_given == "") or (angle1_given == "" and angle3_given == "") or (angle2_given == "" and angle3_given == "") or (angle1_given == "" and angle2_given == "" and angle3_given == ""):
    print("Insufficient data acquired, cannot compute.")
    exit()
if (angle1_given != "" and (angle1_given <= 0 or angle1_given >= 180) or angle2_given != "" and (angle2_given <= 0 or angle2_given >= 180) or angle3_given != "" and (angle3_given <= 0 or angle3_given >= 180)):
    print("Impossible angle attained, Triangle destroyed.")
    exit()
    
import math

if side1 == "" and (angle1 == 90 or angle2 == 90 or angle3 == 90):
    side1 = (side3 ** 2 - side2 ** 2) ** (1 / 2)
if side2 == "" and (angle1 == 90 or angle2 == 90 or angle3 == 90):
    side2 = (side3 ** 2 - side1 ** 2) ** (1 / 2)
if side3 == "" and (angle1 == 90 or angle2 == 90 or angle3 == 90):
    side3 = (side1 ** 2 + side2 ** 2) ** (1 / 2)
if side1 == "" and (angle1 != 90 and angle2 != 90 and angle3 != 90):
    side1 = side2 * math.cos(math.radians(angle1)) + math.sqrt(side3 ** 2 - side2 ** 2 * math.sin(math.radians(angle1)))
if side2 == "" and (angle1 != 90 and angle2 != 90 and angle3 != 90):
    side2 = side1 * math.cos(math.radians(angle1)) + math.sqrt(side3 ** 2 - side1 ** 2 * math.sin(math.radians(angle1)))
if side3 == "" and (angle1 != 90 and angle2 != 90 and angle3 != 90):
    side3 = ((side1 ** 2 + side2 ** 2) - (2 * side1 * side2 * math.cos(math.radians(angle1)))) 

if angle1 == "":
    angle1 = 180 - (angle2 + angle3)
if angle2 == "":
    angle2 = 180 - (angle1 + angle3)
if angle3 == "":
    angle3 = 180 - (angle1 + angle2)
if (angle1 <= 0 or angle2 <= 0 or angle3 <= 0):
    print("returned angle non-real, triangle destroyed.")
    exit()


if side1_given != "" and side2_given != "":
    print("If side one = " + str(side1) + " and side two = " + str(side2) + ", then side three = " + str(side3))
if side1_given != "" and side3_given != "":
    print("If side one = " + str(side1) + " and side three = " + str(side3) + ", then side two = " + str(side2))
if side2_given != "" and side3_given != "":
    print("If side two = " + str(side2) + " and side three = " + str(side3) + ", then side one = " + str(side1))
    
print("Angle 1: " + str(angle1) + " Angle 2: " + str(angle2) + " Angle 3: " + str(angle3))

area = (side1 * side2) * math.sin(math.radians(angle1)) / 2 
height = area * 2 / side1
print("Area = " + str(area) + "\nHeight = " + str(height))

if((side1 == side2) and (side1 == side3) and (side2 == side3)):
    print("Equilateral Triangle.")
if(((side1 == side2) or (side1 == side3) or (side2 == side3)) and not(side1 == side2 and side1 == side3 and side2 == side3)):
    print("Isosceles Triangle.")
if(side1 != side2 and side1 != side3 and side2 != side3):
    print("Scalene Triangle")
if(angle1 != 90 and angle2 != 90 and angle3 != 90):
    print("Acute Triangle")
if(angle1 == 90 or angle2 == 90 or angle3 == 90):
    print("Right Triangle")
if(angle1 > 90 or angle2 > 90 or angle3 > 90):
    print("Obtuse Triangle")
 

