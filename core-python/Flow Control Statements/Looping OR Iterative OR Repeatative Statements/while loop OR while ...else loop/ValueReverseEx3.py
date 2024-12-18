#Program for Obtaining the Reverse of a Given Numerical Value--Logic-3
#ValueReverseEx2.py
n=int(input("Enter Any Numerical Value:"))
print("Given Value:{}".format(n))
rn=0
while(n>0):
    r=n%10
    rn=rn*10+r
    n=n//10
else:
    print("Reversed Value={}".format(rn))

