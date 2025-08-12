#Write a Python program to parse a string to float or integer.

string_value= input("please, enter any value: \n")

try:
    if '.' in string_value:
        result = float(string_value)
    else:
        result= int(string_value)
    print(f"the parsed value {string_value} is {result}, and the datatype is", type(result))
except ValueError:
    print(f"the input {string_value} is not a number")