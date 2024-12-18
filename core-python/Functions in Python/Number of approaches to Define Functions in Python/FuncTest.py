# Program for Demonstrating The Parts of Functions
print("Line-2: I am before Function Definition")
def greet(name): # Function Definition
    print("Line-3: {} Good Morning".format(name))

print("Line-6--->I am from main program and after function def")
greet("Rossum") # Function Call
print("Line-8--->I am from main program and after function Call")
print("------------------------------")
greet("Travis") # Function Call
greet("John Hunter") # Function Call
print("------------------------------")
#welcme()----NameError: name 'welcme' is not defined