#Program for Accepting a Word and Decide whether It is Vowel Or Not
#BreakEx6.py
word=input("Enter a Word:")
if(len(word)==0):
    print("Word should not be empty-try again")
else:
    if(word.isspace()):
        print("Word should not be space-try again")
    else:
        res="NOT VOWEL WORD"
        for ch in word:
            if ch.lower() in list("aeiou"):
                res="VOWEL WORD"
                break
        print("{} is {}".format(word,res))

