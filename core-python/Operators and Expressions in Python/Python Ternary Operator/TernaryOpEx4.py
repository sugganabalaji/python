#Program for Accepting Three Numerical values and Find Biggest among them and check for equality.
#TernaryOpEx4.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=float(input("Enter Third Value:"))
big=a if b<=a>c else b if a<b>=c else c if a<=c>b else "ALL VALS ARE EQUAL"
print("Big({},{},{})={}".format(a,b,c,big))

