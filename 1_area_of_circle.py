#QUESTION

#Write a Python program that calculates the area of a circle based on the radius
#entered by the user.
'''
Area of a circle= pi * (raduis ** 2)
where pi=22/7
raduis = input by the user

assign variables
'''
pi= 22/7
raduis = float(input("raduis:\n"))
try:
    area=  pi * (raduis ** 2) 
    print("The Area of the circle is", area)
except:
    print("invalid input as raduis")

