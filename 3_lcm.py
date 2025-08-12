'''Write a Python program to find the least common multiple (LCM) of two positive
integers. enter by the user from the terminal
'''

import math
try:
    num_1=int(input("enter the first number: "))
    num_2=int(input("enter the second number: "))
    if num_1<=0 or num_2<=0:
        print("enter positive values")
    else:
        lcm=math.lcm(num_1, num_2)
        print(f"{lcm} is the lowest common multiple")
except ValueError:
    print("enter positive numbers")