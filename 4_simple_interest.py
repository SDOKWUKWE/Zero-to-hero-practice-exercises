#Write a Python program to compute the future value of a specified principal
#amount, rate of interest, and number of years. (calculate simple interest based on
#user input)

#simple interest denoted as S_i= P * (r/100) * t
#P = principal or amount deposited
# R= rate in percentage
# T = time accrued

#assign variables requiring user input

principal = float(input("amount: "))
rate = float(input("interest rate: "))
time = int(input("times: "))

simple_intrest= principal * (rate/100) * time

print("Simple interest=", simple_intrest)