#program for accepting List of Values and Obtains Unique Values
#UniqueListValuesEx1.py
nov=int(input('Enter How Many values u Have:'))
if(nov<=0):
    print("\t{} Invalid input".format(nov))
else:
    lst=[] # empty List for adding values
    for i in range(1,nov+1):
        lst.append(float(input("Enter {} Value:".format(i))))
    else:
        print("Given List of Elements")
        print(lst) # [10.0, 20.0, 10.0, 20.0, 30.0, 10.0]
        #Logic for Obtaining Unique Values
        ulist=list()  # for adding Unique Values
        for val in lst:
            if val not in ulist:
                ulist.append(val)
        else:
            print("Unique Elements")
            print(ulist)
