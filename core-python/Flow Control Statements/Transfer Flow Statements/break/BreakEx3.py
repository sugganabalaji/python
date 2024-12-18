#Program for Demonstrating the need fo break statement--while loop
#BreakEx3.py
s="MISSISSIPPI"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("I am from else part of for loop")
    print("----------------------------------")
#My Requirement is to display only "MISS" without using Indexing and Slicing
ctr=0
for ch in s:
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print(ch,end="")
else:
    print("I am from else part of for loop")
print("\nOther statements in Program")

