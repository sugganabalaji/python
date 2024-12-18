#Program for finding Product of n Natural Numbers
#WhileLoopEx7.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-" * 50)
    print("Natural Numbers within:{}".format(n))
    print("-" * 50)
    i=1
    p=1 # Called Multiplicative Identity used for accumulating product of Dynamic generated Values
    while(i<=n):
        print("\t{}".format(i))
        p = p * i
        i=i+1
    else:
        print("-"*50)
        print("Product={}".format(p))
        print("-" * 50)