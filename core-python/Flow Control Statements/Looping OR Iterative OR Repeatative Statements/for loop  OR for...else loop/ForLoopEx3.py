#Program for generating Mul Table for a Given Number
#ForLoopEx3.py
n=input("Enter a Number for Generating Multiplication Table:")
if(n.isdigit()):
    n=int(n)
    if(n==0):
        print("{} is Invalid Input".format(n))
    else:
        print("="*50)
        print("\tMul Table for:{}".format(n))
        print("=" * 50)
        for i in range(1,11):
            print("\t{} x {}={}".format(n,i,n*i))
        else:
            print("=" * 50)
else:
    print("{} is Invalid Input".format(n))