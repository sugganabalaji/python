#Program for accepting a Number and Decide wether It is palindrome or not
#NumberPalindromeEx1.py
n=int(input("Enter Any Numerical Value:"))
print("Given Value:{}".format(n))
rn=0
tn=n # We are Preserving n value in another Temp var ie. tn
while(n>0):
    r=n%10
    rn=rn*10+r
    n=n//10
else:
    if(tn==rn):
        print("{} is Palindrome".format(tn))
    else:
        print("{} is Not Palindrome".format(tn))


