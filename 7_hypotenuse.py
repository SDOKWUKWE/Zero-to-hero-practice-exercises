#Write a Python program to calculate the hypotenuse of a right angled triangle.
#to find the hypotenuse of a right angled triangele, you use the formula

# a**2= (b**2)+ (c**2)
#where a = hypotenus
#b= base
#c= perpendicular side

#assign variables
#apply the input function
import math

b=float(input("base value: "))
c=float(input("perpendicular value: "))

a= (b**2) + (c**2)

#find square_root of a
square_root= math.sqrt(a)
print("Hypotenus is", square_root)


