
#TernaryOpEx7.py
x=input("Enter a Character:")
res="Vowel" if x in tuple("AEIOUaeiou") else "Not Vowel"
print("{} is {}".format(x,res))