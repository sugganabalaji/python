#Program for accepting a Digit and Display Its Name by using if..elif..else statement
#DigitsEx5.py
d1={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",
    -1:"-ONE",-2:"-TWO",-3:"-THREE",-4:"-FOUR",-5:"-FIVE",-6:"-SIX",-7:"-SEVEN",-8:"-EIGHT",-9:"-NINE"}
dig=int(input("Enter the Digit:"))
print("{} is {}".format(dig,d1.get(dig) if d1.get(dig)!=None else "+VE NUMBER" if dig>9 else "-VE NUMBER"))
