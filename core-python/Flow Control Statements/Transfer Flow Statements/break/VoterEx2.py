#Program for Deciding weather the citizen is Eligible Vote Or Not
#VoterEx2.py
while(True):
    age=int(input('Enter Ur Age:'))
    if(age>=18):
        print("\t{} Years Citizen is Elibile to Vote".format(age))
        break
    else:
        print("\t{} Years Citizen is Not Elibile to Vote".format(age))

