'''
Write a Python program to check if a triangle is equilateral, isosceles or
scalene.
#Note 
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
'''

#Assign variables say, a, b, and c marking the sides of a triangle
#request for user input

a=float(input("side a: "))
b=float(input("side b: "))
c=float(input("side c: "))

if a==b==c:
    print("It's an Equilateral triangle")
elif a==b or b==c or c==a:
    print("It's an Isosceles triangle")
else:
    print("It's a Scalene triangle")
