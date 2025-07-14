#Write a program to determine the price of a movie ticket.
#The base price is $12 for adults (age 18 and over) and $8 for children.
#If it's a weekend, add $2 to the price.
#Ask the user for their age and if it is a weekend (e.g., they can enter 'yes' or'no').

adults=float(12.00)
children=float(8.00)
#adults must be greater than 18 years

#for weekends
weekend_1=adults + 2.00
weekend_2=children + 2.00

age=int(input("age:"))
weekend=str(input("Is it weekend? Yes or No:"))

if age >=18:
    if weekend=="Yes":
        print(f"Your movie ticket costs ${weekend_1}")
    else:
        print(f'Your movie ticket costs ${adults}')
if age <18:
    if weekend=="Yes":
        print(f"Your movie ticket costs ${weekend_2}")
    else:
        print(f"Your movie ticket costs ${children}")
