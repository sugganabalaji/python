#Program for Accepting Three Numerical values and Find Biggest among them and check for equality.
#TernaryOpEx3.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=float(input("Enter Third Value:"))
big=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "all vals are equal"
print("Big({},{},{})={}".format(a,b,c,big))

