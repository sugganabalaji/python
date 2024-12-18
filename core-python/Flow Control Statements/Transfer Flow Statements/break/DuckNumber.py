#DuckNumber.py
num=input("Enter a Number for Deciding whether It is Duck OR Not:")
if(num[0]=='0'):
    print("{} is Not Duck Number".format(num))
else: # n=3210
    res="Not Duck"
    for d in num:
        if(d=="0"):
            res="Duck"
            break
    print("{} is {}".format(num,res))





