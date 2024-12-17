#Program for Accepting Two Numerical values and Find Biggest among them and check for equality.
#TernaryOpEx2.py
a,b=float(input("Enter Value of a:")),float(input("Enter Value of b:"))
res= a if a>b else b if b>a else "Both Values are Equal"
print("Big({},{})={}".format(a,b,res))