#Program for accepting a Number and Its Digits sum
#SumOfDigitsEx1.py
num=int(input("Enter a Number:")) # 2356
if(num<=0):
    print("{} is Invalid Input:")
else:
    ds=0
    for d in str(num):
        ds=ds+int(d)
    else:
        print("SumOfDigits({})={}".format(num,ds))

