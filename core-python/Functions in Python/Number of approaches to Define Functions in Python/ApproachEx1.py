#Program for Calculting Sum of Two Numbers by using Functions
#ApproachEx1.py
def sumop(k,v): # Here k and v are called Formal Params
    r=k+v # Here r is called Local Variable
    return r


#Main Program
res=sumop(10,20) # Function Call
print("sum=",res)
r=sumop(100,200)
print("sum=",r)
r=sumop(-10,-300)
print("sum=",r)