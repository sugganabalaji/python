#Program for finding Max Word Length in a Line of Text:
#MaxWordLengthEx1.py
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
           vals=dw.values()
           print('----------------------------')
           print("Largest Word Length")
           print('----------------------------')
           for word,wordlen in dw.items():
               if(wordlen==max(vals)):
                   print("'{}'".format(word))
           print('----------------------------')
