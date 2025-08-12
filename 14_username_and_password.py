#Create a simple login system.
# Define a username and password in your code. 
# Ask the user to enter their username and password.
# If they match the predefined credentials, print "Login successful." Otherwise, print "Invalid credentials."

#assign variables for data in database

user_id="Mybaby101"
password="Baby0910"

#input details
user_name= str(input("Username:"))
pass_word= str(input("Password:"))

#use if statement
if user_name==user_id and password==pass_word:
    print(f"Welcome {user_id}!")
    print("Login successsful!")
else:
    print("Invalid User ID")
    print("Login Unsuccessful")