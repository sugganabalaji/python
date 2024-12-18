#Program for Generating Even Numbers within n where n is +ve
#WhileLoopEx3.py
n=int(input("Enter How Many Range in which u want even Numbers:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-"*50)
    print("List of Even Numbers within {}".format(n))
    en=2 # Initialization Part
    while(en<=n):
        print(en)
        en=en+2
    else:
        print("-" * 50)
