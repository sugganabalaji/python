#Program for Displaying every Character from str object by using for loop
#ForLoopEx1.py
s=input("Enter a Line of Text:") # here s is called Iterable Object
print('----------------------------------------')
print("By using for Loop--Forward direction")
print('----------------------------------------')
for ch in s:  # PYTHON
    print(ch)
print('---------------OR-------------------------')
for i in range(len(s)):
    print(s[i])
print('---------------OR-------------------------')
for i in range(-len(s),0):
    print(s[i])
print('----------------------------------------')
print("By using for Loop--Backward direction")
print('----------------------------------------')
for ch in s[::-1]:
    print(ch)
print('---------------OR-------------------------')
for i in range(len(s)-1, -1, -1):
    print(s[i])
print('---------------OR-------------------------')
for i in range(-1, -(len(s)+1),-1):
    print(s[i])
