#Program for Generating 1 to n where n is Possitive
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=1 # Initlization Part
    while(i<=n): # Cond Part
        print(i)
        i=i+1 # Updation Part
    else:
        print("i am from else part of while loop")
    print("while loop execution Over")
print("I am from if...else stmt")

