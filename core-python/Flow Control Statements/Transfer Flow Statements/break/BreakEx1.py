#Program for Demonstrating the need fo break statement--for loop
#BreakEx1.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("I am from else part of for loop")
    print("----------------------------------")
#My Requirement is to display only "PYTH" without using Indexing and Slicing
print("By using for loop with break")
for ch in s:
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("I am from else part of for loop")
print()
print("Other statements in Program")