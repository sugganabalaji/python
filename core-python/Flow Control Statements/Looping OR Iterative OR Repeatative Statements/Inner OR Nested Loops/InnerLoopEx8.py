#program for generating Primes within the range n
#InnerLoopEx8.py
n=int(input("Enter the Range in which primes will de displayed:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    print("-----------------------------------")
    print("List of Prime Numbers")
    print("-----------------------------------")
    nop=0
    for num in range(2,n+1):# inner loop---supply the Number
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t\t{}".format(num))
            nop=nop+1
    else:
        print("-----------------------------------")
        print("Number of Primes within {}={}".format(n,nop))
        print("-----------------------------------")


