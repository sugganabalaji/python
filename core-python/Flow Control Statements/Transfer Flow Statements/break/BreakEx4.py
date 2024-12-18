#Program for Deciding whether the given Number is prime or not
#BreakEx4.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid input:".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))

