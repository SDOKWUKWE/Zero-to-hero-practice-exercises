

def gcd (a,b):
    while b:
        a,b=b, a%b
        return a
num_1=int(input())
num_2=int(input())

if num_1<=0 or num_2<=0:
    print("enter positive values")
else:
    result=gcd(num_1,num_2)
    print(result)