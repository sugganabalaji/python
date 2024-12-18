#ContinueEx2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("i am from else part of while loop")
print("-----------------------------------------")
#My Reqriment is to display :  PYHON
print("By using while loop with continue stmt")
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="T"):
        i = i + 1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("\ni am from else part of for loop")
print("-----------------------------------------")