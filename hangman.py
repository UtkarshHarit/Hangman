import random
import sys
word=input("Enter the word: ")

size=len(word)
print(size)

x1=random.randint(0,size)
x2=random.randint(0,size)
new_word=word
new_word2=[]
print(new_word)

for a in word:
    new_word2.extend(["_"])

new_word2[x1-1]=new_word[x1-1]
new_word2[x2-1]=new_word[x2-1]

print(new_word2)
chance=5

while(chance!=0):
    x=input("Enter an character: ")
    nest=[]
    for d in word:
        nest.extend([d])
    if(x in word):
        l=word.index(x)
        new_word2[l]=x
        print(new_word2)
        if(new_word2==nest):
            print("Congratulations!! you won...")
            sys.exit()
    else:
        chance=chance-1
        print("Wrong you have %d chance left" %chance)
        if(chance==0):
            print("Sorry you loose!!!!!")
            sys.exit()
