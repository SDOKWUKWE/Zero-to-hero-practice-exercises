#A shop offers a 10% discount if the total bill is over $100. 
# Write a program that asks for the total bill amount and prints the final amount to be paid 
# after the discount, if applicable.


discount_value=10
total_bill=float(input("Bill:"))
discount=(total_bill/100)*(discount_value)
final_amt=total_bill-discount

if total_bill>100:
    print(f"Your final amount is {final_amt}$, enjoy your 10% discount!")
else:
    print(f"Your total bill is {total_bill}$")
