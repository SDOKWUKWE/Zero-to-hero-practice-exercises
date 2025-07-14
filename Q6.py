#Write a Python program to convert height (in feet and inches) to centimeters.


Height_in_ft= float(input("height(ft)" ))
Height_in_inches = float(input("height(inches)" ))

height_in_cm1= float(Height_in_ft * 30.48)

height_in_cm2= float(Height_in_inches * 2.54)

if Height_in_ft:
    print("height is:",height_in_cm1,"ft")
    
else:
    print("height is",height_in_cm2,"cm")