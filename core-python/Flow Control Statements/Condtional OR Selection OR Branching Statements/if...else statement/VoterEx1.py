#Program for Deciding weather the citizen is Eligible Vote Or Not
#VoterEx1.py
age=int(input('Enter Ur Age:'))
if(age<18):
    print("\t{} Years Citizen is Not Eligible to Vote:".format(age))
else:
    print("\t{} Years Citizen is Eligible to Vote:".format(age))
