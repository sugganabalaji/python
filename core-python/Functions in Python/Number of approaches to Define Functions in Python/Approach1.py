#Program for Calculting Sum of Two Numbers by using Functions
#Approach1.py
#INPUT   :  Taking from Function Call
#PROCESS :  Inside Function Body
#OUTPUT  : Giving to Function call
def sumop(k,v): # Here k and v are called Formal Params
    r=k+v # Here r is called Local Variable
    return r

#Main Program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
res=sumop(x,y) # Function Call is Taking inputs and Getting output
print("sum({},{})={}".format(x,y,res))
print("-------------------------------------")
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
r=sumop(k,v) # Function Call
print("sum({},{})={}".format(k,v,r))
