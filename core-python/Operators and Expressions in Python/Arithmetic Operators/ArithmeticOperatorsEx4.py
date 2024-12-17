#ArithmeticOperatorsEx4.py
#Celsius to Fahrenheit	° F = 9/5 ( ° C) + 32
#Kelvin to Fahrenheit	° F = 9/5 (K - 273) + 32
ct=float(input("Enter the Temp in Celsius:"))
F = (9/5)* ct + 32
print("Celsius in Fahrenheit={}".format(F))
print("---------------------------------------")
kt=float(input("Enter the Temp in Kelvin:"))
F = (9/5)*(kt - 273) + 32
print("Kelvin in Fahrenheit={}".format(F))

