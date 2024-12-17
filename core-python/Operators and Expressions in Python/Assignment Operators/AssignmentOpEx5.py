#Write a Python Program which will swap Two Values--Logic-5
#AssignmentOpEx5.py
#This Program works for Swapping of Numerical Values
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-----------------------------")
print("Original Value of a={}".format(a))
print("Original Value of b={}".format(b))
print("-----------------------------")
#Swapping Logic by using Bitwise XOR Operator
a=a^b
b=a^b
a=a^b
print("Swapped Value of a={}".format(a))
print("Swapped Value of b={}".format(b))
print("-----------------------------")


