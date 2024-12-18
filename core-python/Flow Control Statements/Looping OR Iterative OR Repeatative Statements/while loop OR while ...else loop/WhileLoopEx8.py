#Program for finding  Factorial of a Given number
#WhileLoopEx8.py
#n!= 1 x 2 x 3 x.....n
n=int(input("Enter Number for Cal Factorial:"))
if(n<0):
    print("{} is Invalid Input:".format(n))
else:
    p=1
    i=1
    while(i<=n):
        p = p * i
        i=i+1
    else:
        print("-"*50)
        print("Factorial({})={}".format(n,p))
        print("-" * 50)