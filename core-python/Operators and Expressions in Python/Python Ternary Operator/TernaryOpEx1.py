#Program for Reading the Value from KBD and Decide whether It is Palindrome or Not
#TernaryOpEx1.py
value=input("Enter a Value:")
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("{} is {}".format(value,res))


