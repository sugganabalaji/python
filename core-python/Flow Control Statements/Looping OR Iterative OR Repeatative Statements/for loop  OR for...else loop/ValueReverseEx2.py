#Program for Obtaining the Reverse of a Given Value--Logic-2
#ValueReverseEx2.py
val=input("Enter Any Value:")
print("Given Value:{}".format(val))
rval=""
for v in val[::-1]:
    rval=rval+v
else:
    print("Reversed Value=",rval)