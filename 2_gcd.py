#Qouestion Write a Python program that computes the greatest common divisor (GCD) of
#two positive intege


import math
try:
    num_1=int(input("enter the first number: "))
    num_2=int(input("enter the second number: "))
    if num_1<=0 or num_2<=0:
        print("enter positive values")
    else:
        gcd=math.gcd(num_1, num_2)
        print(f"{gcd} is the greatest common divisor")
except ValueError:
    print("enter positive numbers")