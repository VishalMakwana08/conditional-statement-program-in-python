# Determine if a triangle is valid based on its angles.


# Input: angles of the triangle
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

# Condition for a valid triangle:
# 1. Sum of angles = 180
# 2. All angles > 0
if (angle1 + angle2 + angle3 == 180) and (angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("The triangle is valid.")
else:
    print("The triangle is NOT valid.")
