
#Write a program that takes three numbers as input and prints the largest one
#using if-elif-else.

#assign variables
#asking for user input

num_1=float(input("Number 1:"))
num_2=float(input("Number 2:"))
num_3=float(input("Number 3:"))

#use if statement
if num_1>num_2 and num_3:
    print(num_1)
elif num_2>num_1 and num_3:
    print(num_2)
elif num_3>num_2 and num_1:
    print(num_3)
elif num_1==num_2==num_3:
    print("Numbers are equal")
elif num_1==num_2:
    print(num_1)
else:
    print("error")