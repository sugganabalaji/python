#Program for accepting Numerical Value and find smallest among them anc check for equality
#SimpleIfStmtEx2.py
print("Enter Two values")
a,b=float(input()),float(input())
if(a<b):
    print("min({},{})={}".format(a,b,a))
if(b<a):
    print("min({},{})={}".format(a,b,b))
if(a==b):
    print("min({},{})={}".format(a,b,"Both value are equal"))
print("Program execution completed")


