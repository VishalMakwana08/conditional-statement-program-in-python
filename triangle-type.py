# Check if a triangle is equilateral, isosceles, or scalene using side lengths.

# Input: sides of the triangle
a = float(input("Enter first side length: "))
b = float(input("Enter second side length: "))
c = float(input("Enter third side length: "))

# First, check if the sides form a valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Classify the triangle
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")
