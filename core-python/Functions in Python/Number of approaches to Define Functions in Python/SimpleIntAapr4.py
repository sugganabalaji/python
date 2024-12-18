#Program for Calculuating Simple Int and total amount to pay by using Functions
#SimpleIntAapr4.py
def simplint():
    #Taking Input Inside of Function Body
    p=float(input("Enter Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    if(p<=0) or (t<=0) or (r<=0):
        return "Invalid Input"
    else:
        # Do the Process
        si=(p*t*r)/100
        totamt=p+si
        #give the result to Function Call
        return p,t,r,si,totamt
#main Program
res=simplint() # Function Call--returns either str or tuple type
if(type(res)==str):
    print(res)
else:
    # Here res is an object of <class, tuple>
    print("===========================================")
    print("\t\t\tSimple Interest Calculations")
    print("===========================================")
    print("\t\tPrinciple Amount:{}".format(res[0]))
    print("\t\tTime:{}".format(res[1]))
    print("\t\tRate of Interest:{}".format(res[2]))
    print("\t\tSimple Interest:{}".format(res[3]))
    print("\t\tTotal Amount to Pay:{}".format(res[4]))
    print("===========================================")