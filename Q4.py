#Write a Python program to compute the future value of a specified principal
#amount, rate of interest, and number of years. (calculate simple interest based on
#user input)

#simple interest denoted as S_i= P * (r/100) * t
#P = principal or amount deposited
# R= rate in percentage
# T = time accrued

#assign variables requiring user input

P = float(input("amount:"  ))
R = float(input("interest rate:"  ))
T = int(input("times:" ))

S_i= P * (R/100) * T

print("Simple interest=", S_i)