#InnerLoopEx2.py----for loop in while loop
i=1
while(i<=5): # Outer loop
    print("*"*50)
    print("Outer loop: Value of i=",i)
    print("*" * 50)
    j=1
    while(j<=3): # Inner loop
        print("\t\tInner loop: Value of j=", j)
        j=j+1
    else:
        i=i+1
        print("\tOut-off inner loop")
        print("-"*50)
else:
    print("Out-off Outer loop")
    print("*" * 50)


