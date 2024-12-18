#PosNegNumsSumEx1.py
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
        #Obtaining and Finding +Ve Elements and their sum
        pslist=[]
        ps=0
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
            ps=ps+val
        else:
            print("Possitive Elements={}".format(pslist))
            print("Possitive Elements Sum={}".format(ps))
            print("-----------------------------------")
            # Obtaining and Finding -Ve Elements and their sum
            nglist=list()
            ns=0
            for val in lst:
                if(val>=0):
                    continue
                nglist.append(val)
                ns=ns+val
            else:
                print("Negative Elements={}".format(nglist))
                print("Negative Elements Sum={}".format(ns))
                print("-----------------------------------")
