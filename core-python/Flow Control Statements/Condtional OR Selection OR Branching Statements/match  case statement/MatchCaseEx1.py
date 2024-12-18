#Program for Performing all arithmetic Operations by using match case
#MatchCaseEx1.py
import sys
print("*"*50)
print("\tArithmetic Operations")
print("*"*50)
print("\t\t1.Addition")
print("\t\t2.Subtraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Div")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")
print("*"*50)
ch=int(input("Enter UR Choice:"))
match(ch):
    case 1 :
        print("Enter Two Values for Addition:")
        a,b=float(input()),float(input())
        print("\t\tsum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Subtraction:")
        a, b = float(input()), float(input())
        print("\t\tsub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication:")
        a, b = float(input()), float(input())
        print("\t\tmul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division:")
        a, b = float(input()), float(input())
        print("\t\tNormal Div({},{})={}".format(a, b, a / b))
        print("\t\tFloor Div({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter Two Values for Modulo Div:")
        a, b = float(input()), float(input())
        print("\t\tmod({},{})={}".format(a, b, a % b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("\t\tpow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for Using this Program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Match case completed")

