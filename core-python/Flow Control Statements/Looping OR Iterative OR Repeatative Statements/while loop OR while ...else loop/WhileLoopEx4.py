#Program for generating Mul table for a given +Ve Integer Value
#hileLoopEx4.py
n=input("Enter a Number for Generating Mul Table:")
if(n.isdigit()):
    n=int(n)
    if(n==0):
        print("{} is Invalid Input".format(n))
    else:
        print("="*50)
        print("\tMul Table for:{}".format(n))
        print("=" * 50)
        i=1
        while(i<=10):
            print("\t\t{}x{}={}".format(n,i,n*i))
            i=i+1
        else:
            print("=" * 50)
else:
    print("{} is Invalid Input".format(n))