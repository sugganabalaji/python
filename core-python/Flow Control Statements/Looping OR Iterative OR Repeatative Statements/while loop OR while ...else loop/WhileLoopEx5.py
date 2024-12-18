#Program for computing sum of N Natural Numbers
#WhileLoopEx5.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-" * 50)
    print("Natural Numbers within:{}".format(n))
    print("-" * 50)
    i=1
    s=0 # Called Additive Identity used for accumulating Sum of Dynamic generated Values
    while(i<=n):
        print("\t{}".format(i))
        s = s + i
        i=i+1

    else:
        print("-"*50)
        print("Sum={}".format(s))
        print("-" * 50)