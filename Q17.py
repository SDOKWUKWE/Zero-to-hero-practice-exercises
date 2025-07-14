#Simulate a simple ATM.
#Initialize a balance, say $1000.
#Ask the user what they want to do: 'withdraw', 'deposit', or 'check balance'.
#If they choose 'withdraw', ask for the amount and subtract it from the balance,but only if they have enough funds.
#If they choose 'deposit', ask for the amount and add it to the balance.
#If they choose 'check balance', display the current balance.
#Handle invalid input gracefully.

Balance=float(1000)
print("A. Withdraw")
print("B. Deposit")
print("C. Check balance")

Select= str(input("select an option: "))
if Select=="A":
    amt=int(input("Amount:"))
    if Balance>amt:
        print("New balance:", Balance-amt)
    else:
        print("insuffecient balance")
if Select=="B":
    amt_2=int(input("Amount:"))
    print("New balance", amt_2 + Balance)
if Select=="C":
    print(Balance)


        