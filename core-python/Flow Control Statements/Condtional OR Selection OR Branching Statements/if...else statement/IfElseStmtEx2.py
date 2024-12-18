#Program for accepting a Value  and Decide whether It is  palindrome or not
#IfElseStmtEx2.py
n=input("Enter a Number:")
if(n==n[::-1]):
    print("{} is Palindrome".format(n))
else:
    print("{} is not Palindrome".format(n))
print("Program execution completed")