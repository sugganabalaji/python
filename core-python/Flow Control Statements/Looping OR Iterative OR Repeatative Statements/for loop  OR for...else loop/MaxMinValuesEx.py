#Program for Finding Max and Min from List of Values
#MaxMinValuesEx.py
n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    lst=[] # create an empty list for adding dynamic values
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        max=lst[0]
        min=lst[0]
        for val in lst:
            if(val>max):
                max=val
            if(val<min):
                min=val
        else:
            print("Given values={}".format(lst))
            print("Max value={}".format(max))
            print("Min value={}".format(min))