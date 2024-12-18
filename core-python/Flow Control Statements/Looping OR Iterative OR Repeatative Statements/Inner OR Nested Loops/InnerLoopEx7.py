#generate 12 Calendar for an Year
#InnerLoopEx7.py
import calendar
year=int(input("Enter an Year:"))
if(year<=0):
    print("Invalid Year:")
else:
    print("-"*50)
    print("Year:{}".format(year))
    print("-" * 50)
    for i in range(1,13):
        print(calendar.month(year,i))
    print("-" * 50)