#Program for Finding Sum and Average for List of Values--Sol2
#ForLoopEx5.py
n=int(input("Enter How Many Value Sum and Avg u want to Find:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    s=0
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        s=s+val
    else:
        print("Sum={}".format(s))
        print("Average=%0.2f" %(s/n))

