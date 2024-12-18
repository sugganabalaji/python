#InnerLoopEx4.py----while loop in for loop
for i in range(1,6): # Outer loop
    print("*"*50)
    print("Outer loop: Value of i=",i)
    print("*" * 50)
    j=3
    while(j>=1): # Inner loop
        print("\t\tInner loop: Value of j=", j)
        j=j-1
    else:
        print("\tOut-off inner loop")
        print("-"*50)
else:
    print("Out-off Outer loop")
    print("*" * 50)


