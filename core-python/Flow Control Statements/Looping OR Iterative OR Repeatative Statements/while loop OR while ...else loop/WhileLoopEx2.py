#Program for generating n to 1 where n is +Ve value
#WhileLoopEx2.py
n=input("Enter How Many Numbers u want generate:")
if(n.isdigit()):
    num=int(n)
    if(num==0):
        print("7--->{} is invalid Input:".format(num))
    else:
        print("--------------------------------")
        print("Numbers from {} to 1".format(num))
        i=num # Initialization
        while(i>=1):
            print(i)
            i=i-1
        else:
            print("--------------------------------")
else:
    print("18---{} is Invalid Input".format(n))
