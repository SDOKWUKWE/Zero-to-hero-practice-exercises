#Write a Python program to convert height (in feet and inches) to centimeters.

#assign variables
#to convert height from feet to cm, multiply by 30.48
#to convert from inches, multiply by 2.54
try:
    Height_feet= float(input("height(ft): \n"))
    Height_inches = float(input("height(inches):\n"))
    
    feet_to_cm= Height_feet * 30
    inches_to_cm= Height_inches * 2.54
    
    total= feet_to_cm + inches_to_cm
    print(f"your height in cm is {total}")
except ValueError:
    print("incorrect inputs")
