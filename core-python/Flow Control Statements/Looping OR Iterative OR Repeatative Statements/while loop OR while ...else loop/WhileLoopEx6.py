#Program for computing sum of N Natural Numbers and Squares sum and cubes sum also
#WhileLoopEx6.py
n=int(input("Enter How Many Natural Nums Sum u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-" * 70)
    print("Nat Nums\t\tSquares Nat Nums\t\tCubes Nat Nums")
    print("-" * 70)
    i=1
    s=0  # Called Additive Identity used for accumulating Sum of Dynamic generated Values
    ss=0 # Called Additive Identity used for accumulating Sum of Dynamic generated Values
    cs=0 # Called Additive Identity used for accumulating Sum of Dynamic generated Values
    while(i<=n):
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(i,i**2,i**3))
        s = s + i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("-"*70)
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(s,ss,cs))
        print("-" * 70)