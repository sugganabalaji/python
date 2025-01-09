
lst = [10,-20,-30,40,0,-50,60,-70,12]

#plist = []
#for val in lst:
#	if(val > 0 ):
#		plist.append(val)
# print(plist)

#plist = [val for val in lst if val >0]
#print(plist)

def getPositive(val):
    if (val > 0): return True
    else: return False

def getNagative(val):
    if (val > 0): return False
    else: return True

obj1 = filter(getPositive,lst)
print(obj1, type(obj1))
obj2 = filter(getNagative,lst)
print(obj2, type(obj2))
plist = list(obj1)
nlist = tuple(obj2)
print(plist, type(plist))
print(nlist, type(nlist))



