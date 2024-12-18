#Program for accepting List of Numerical values and Find only +Ve Values
#ContinueEx4.py
nov=int(input("Enter How Many Values u have:"))
if(nov<=0):
    print("{} is Invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val=float(input("Enter {} Values:".format(i)))
        lst.append(val)
    else:
        print("Given List of Values")
        print(lst)#[100.0, -200.0, 300.0, -150.0, 40.0]
        print("-----------------------------------")
        pslist=[]
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
        print("-----------------------------------")
        print("List of +Ve Values")
        print(pslist)
