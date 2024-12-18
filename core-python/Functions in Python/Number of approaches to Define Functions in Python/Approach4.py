#Program for Calculating Sum of Two Numbers by using Functions
#INPUT    : Taking Inside of function body
#PROCESS  :  Inside of function body
#OUTPUT   :  Giving to Function call
#Approach4.py
def sumop():
    # Taking Input
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Doing the Process
    c = a + b
    #give the result back to function call
    return a,b,c # return stmt can return Not only one value but also returns more than one value

#Main Program
a,b,res=sumop() # Function call with multi line --Not taking Input But returning the Result
print("sum({},{})={}".format(a,b,res))
print("------------OR---------------")
res=sumop() # Function call with single line --Not taking Input But returning the Result
#here res is an object of type <class, tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("------------OR---------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))
