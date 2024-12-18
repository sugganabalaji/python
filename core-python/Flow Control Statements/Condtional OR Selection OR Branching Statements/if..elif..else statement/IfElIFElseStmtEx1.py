#Program for accepting a Number and Decide whether It is Even Or Odd for +ve Number Only
#IfElIFElseStmtEx1.py
n=int(input("Enter a Number:")) # n=-4
if(n<=0):
    print("{} is Invalid input:".format(n))
elif(n%2==0):
        print("{} is Even".format(n))
elif (n % 2 != 0):
     print("{} is Odd".format(n))
print("I am from  if..elif...else statement")
