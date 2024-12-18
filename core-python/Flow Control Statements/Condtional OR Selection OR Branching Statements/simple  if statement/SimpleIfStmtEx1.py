#Program for accepting Numerical Value and Decide whether It is +Ve or -Ve or Zero
#SimpleIfStmtEx1.py
n=float(input("Enter a Numerical value:"))
#n can be +ve  or -ve  or  zero
if(n>0):
    print("{} is +VE".format(n))
if(n<0):
    print("{} is -VE".format(n))
if(n==0):
    print("{} is ZERO".format(n))
print("Program execution completed")