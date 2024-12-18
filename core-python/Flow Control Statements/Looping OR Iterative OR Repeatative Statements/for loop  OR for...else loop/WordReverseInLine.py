#Program for accepting a Line of Text and place reverse of every word in same place of Line
#WordReverseInLine.py
line=input("Enter a Line of Text:")
if(len(line)==0):
    print("Enter a Line of Text--Try again")
else:
    if(line.isspace()):
        print("Dont enter space--try again:")
    else:
        print("----------------------------")
        print("Given Line={}".format(line))
        words=line.split()
        rwl=[]
        for word in words:
            rwl.append(word[::-1])
        else:
            print("Reversed line with Words={}".format(" ".join(rwl)))
            print("----------------------------")


