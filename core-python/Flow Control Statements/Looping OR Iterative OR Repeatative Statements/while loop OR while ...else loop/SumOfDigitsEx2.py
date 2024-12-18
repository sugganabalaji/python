#Program for accepting a Number and Its Digits sum
#SumOfDigitsEx2.py
num=int(input("Enter a Number:")) # 2356
if(num<=0):
    print("{} is Invalid Input:")
else:
    tn=num
    ds=0
    while(num>0):
        d=num%10
        ds=ds+d
        num=num//10
    else:
        print("SumOfDigits({})={}".format(tn,ds))

