word = input()
low = 0 
cap = 0 
for i in word :
    if(i.lower()==i):
        low+=1
    else:
        cap+=1
if(cap>low):
    print(word.upper())
else:
    print(word.lower())