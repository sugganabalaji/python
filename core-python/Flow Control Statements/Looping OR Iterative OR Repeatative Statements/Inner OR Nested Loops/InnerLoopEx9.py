#InnerLoopEx9.py
n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    lst=[] # create an empty list for adding dynamic values
    for i in range(1,n+1):
        val=int(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Values")
        print(lst) # [19, -4, 0, 18, 8]
        for num in lst: # Outer loop
            if(num<=0):
                continue
            print("-------------------------------")
            print("Mul Table for :{}".format(num))
            print("-------------------------------")
            for i in range(1,11):#Inner loop
                print("\t{} x {}={}".format(num,i,num*i))
            else:
                print("-------------------------------")


