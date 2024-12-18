#Program for Deciding whether the given Number is prime or not
#BreakEx5.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid input:".format(n))
else:
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime=False
            break
    print("{} is PRIME".format(n) if prime else "{} is NOT PRIME".format(n))

