#program for generating Mul tables for 1 to n where n is +ve
#InnerLoopEx6.py
n=int(input("Enter How Many Mul tables u want:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    for num in range(1,n+1): ## inner loop---supply the Number
        print("-"*50)
        print("Mul Table for:{}".format(num))
        print("-" * 50)
        for i in range(1,11): # inner loop--generates mul table for number supplied by outer loop
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("-" * 50)