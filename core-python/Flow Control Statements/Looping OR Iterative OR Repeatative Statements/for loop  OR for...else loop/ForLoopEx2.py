#ForLoopEx2.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-" * 70)
    print("Nat Nums\t\tSquares Nat Nums\t\tCubes Nat Nums")
    print("-" * 70)
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*70)
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(s, ss, cs))
        print("-" * 70)
