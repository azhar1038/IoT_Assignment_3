from math import sqrt

def area_of_rect(length, breadth):
    return length*breadth

def peri_of_rect(length, breadth):
    return 2*(length+breadth)

def area_of_square(side):
    return side*side

def peri_of_square(side):
    return 4*side

def is_triangle(a, b, c):
    if a+b<=c or a+c<=b or b+c<=a:
        return False
    return True

def area_of_tri(a, b, c):
    if is_triangle(a, b, c):
        s = (a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))
    return "Invalid Triangle"

def peri_of_tri(a, b, c):
    if is_triangle(a, b, c):
        return a+b+c
    return "Invalid Triangle"

l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
print("Area of rectangle:", area_of_rect(l, b))
print("Perimeter of rectangle:", peri_of_rect(l, b))

s = int(input("Enter side of square: "))
print("Area of square:", area_of_square(s))
print("Perimeter of square:", peri_of_square(s))

a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))
print("Perimeter of triangle:", peri_of_tri(a, b, c))
print("Area of triangle:", area_of_tri(a, b, c))