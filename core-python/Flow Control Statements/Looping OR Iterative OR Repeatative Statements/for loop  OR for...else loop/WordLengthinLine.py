#Program for Accepting a Line of Text and File all words length
#WordLengthinLine.py
line=input("Enter a Line of Text:")
if(len(line)==0):
    print("Enter a Line of Text--Try again")
else:
    if(line.isspace()):
        print("Dont enter space--try again:")
    else:
        words=line.split()
        print("Given Line={}".format(line))
        for word in words:
            print("\t\t{}--->{}".format(word,len(word)))
