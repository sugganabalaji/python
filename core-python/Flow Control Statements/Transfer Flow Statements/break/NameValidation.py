#Program for validating tghe Name
#NameValidation.py
name=input("Enter Ur Name:")
print("Given Name:{}".format(name)) # Guido V2an Rossum
#Logic for Validation of Name
words=name.split() # words=['Guido', 'V2an', 'Rossum']
nv=True
for word in words:
    if(not word.isalpha()):
        nv=False
        break
if(nv):
    print("{} is Valid Name:".format(name))
else:
    print("{} is InValid Name:".format(name))
