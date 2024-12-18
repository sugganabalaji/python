#Program for accepting a Number and Decide whether It is Even Or Odd for +ve Number Only
#IfElseStmtEx1.py
n=int(input("Enter a Number:")) # n=-4
if(n<=0):
    print("{} is Invalid input:".format(n))
else:
    if(n%2==0):
        print("{} is Even".format(n))
    else:
        print("{} is Odd".format(n))
    print("I am from inner if..else statement")
print("I am from outer if..else statement")