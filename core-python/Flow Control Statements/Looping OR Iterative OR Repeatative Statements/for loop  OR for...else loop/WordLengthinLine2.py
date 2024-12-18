#Program for Accepting a Line of Text and File all words length
#WordLengthinLine2.py
line=input("Enter a Line of Text:")
if(len(line)==0):
    print("Enter a Line of Text--Try again")
else:
    if(line.isspace()):
        print("Dont enter space--try again:")
    else:
        dw={} # create an empty dict for placing word: its length
        words=line.split()
        for word in words:
            dw[word]=len(word)
        else:
           for w,wl in dw.items():
               print("\t{}-->{}".format(w,wl))




