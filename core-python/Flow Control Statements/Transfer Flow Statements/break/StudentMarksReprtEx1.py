#StudentMarksReprtEx1.py
#Validation of student number
while(True):
    sno=input("Enter Student Number(100-200):")
    if(sno.isdigit()) and (int(sno) in range(100,201)):
        break
    else:
        print("\t{} is Invalid Student Number--try again".format(sno))
#Validation of student Name
while(True):
    name=input("Enter Student Name:")
    words=name.split() # words=['Guido', 'V2an', 'Rossum']
    nv=True
    for word in words:
        if(not word.isalpha()):
            nv=False
            break
    if(nv):
        break
    else:
        print("\t{} is InValid Name:".format(name))
#Validation of C Lang Marks-- 0 to 100
while(True):
    cm=input("Enter C lang Marks(0-100):")
    if(cm.isdigit()) and (0<=int(cm)<=100):
        break
    else:
        print("\t{} is Invalid Marks in C--try again".format(cm))
#Validation of C++ Lang Marks-- 0 to 100
while(True):
    cppm=input("Enter C++ lang Marks(0-100):")
    if(cppm.isdigit()) and (0<=int(cppm)<=100):
        break
    else:
        print("\t{} is Invalid Marks in C++--try again".format(cppm))
#Validation of PYTHON Lang Marks-- 0 to 100
while(True):
    pym=input("Enter PYTHON lang Marks(0-100):")
    if(pym.isdigit()) and (0<=int(pym)<=100):
        break
    else:
        print("\t{} is Invalid Marks in PYTHON--try again".format(pym))
#Calculate TOTMARKS and PERCENTAGE of Marks
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
#Decide the Grade
if(int(cm)<40) or(int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
     if(percent in range(75,101)):
         grade="DISTINCTION"
     elif(percent in range(60,75)):
         grade = "FIRST"
     elif(50<=percent<=59):
         grade="SECOND"
     elif (40<=percent<=49):
         grade = "THIRD"
#display the Student Marks Report
print("*"*70)
print("\t\tSTUDENT MARKS REPORT")
print("*"*70)
print("\t\tStudent Number:{}".format(sno))
print("\t\tStudent Name:{}".format(name))
print("\t\tStudent Marks in C:{}".format(cm))
print("\t\tStudent Marks in C++:{}".format(cppm))
print("\t\tStudent Marks in PYTHON:{}".format(pym))
print("\t\tStudent Total Marks:{}".format(totmarks))
print("\t\tStudent Percentage of Marks:{}".format(percent))
print("\t\tSTUDENT GRADE:{}".format(grade))
print("*"*70)
