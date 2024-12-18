#PosNegNumsSumEx2.py
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
        print(lst)#[10,-20,30,-40,0,-15]
        print("-----------------------------------")
        ps,ns=0,0
        pslist=[]
        nslist=[]
        for val in lst:
            if(val>0):
                ps=ps+val
                pslist.append(val)
            else:
                ns=ns+val
                nslist.append(val)
        else:
            print("Possitive Elements={}".format(pslist))
            print("Possitive Elements Sum={}".format(ps))
            print("-----------------------------------")
            print("Negative Elements={}".format(nslist))
            print("Negative Elements Sum={}".format(ns))
            print("-----------------------------------")