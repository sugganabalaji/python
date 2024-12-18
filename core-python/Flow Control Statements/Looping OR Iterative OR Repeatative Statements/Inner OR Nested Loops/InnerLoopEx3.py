#InnerLoopEx3.py----for loop in while loop
i=5
while(i>=1): # Outer loop
    print("*"*50)
    print("Outer loop: Value of i=",i)
    print("*" * 50)
    for j in range(3,0,-1):  # Inner loop
        print("\t\tInner loop: Value of j=", j)
    else:
        i=i-1
        print("\tOut-off inner loop")
        print("-"*50)
else:
    print("Out-off Outer loop")
    print("*" * 50)


