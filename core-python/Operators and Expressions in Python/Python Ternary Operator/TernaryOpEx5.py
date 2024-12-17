#Program for Accepting a Numerical Integer value and decide whether ift is even or odd
#TernaryOpEx5.py
n=int(input("Enter any Integer Value:"))
res="{} is Invalid Input".format(n) if n<=0 else "{} Even".format(n) if n%2==0 else "{} is Odd".format(n)
print(res)