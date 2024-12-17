#Program for Cal Area of Circle
#CircleAreaEx.py
#Accepting the Input from KBD
r=float(input("Enter Radius:"))
#Process the Input---Calculation--Business Logic
ac=3.14*r*r
#Display the Result
print("*"*50)
print("\t\tRadius={}".format(r))
print("\t\tArea of Circle={}".format(ac))
print("---------------OR----------------")
print("\t\tArea of Circle=%0.2f" %ac)
print("---------------OR----------------")
print("\t\tArea of Circle={} Sq Units".format(round(ac,2)))
print("*"*50)
