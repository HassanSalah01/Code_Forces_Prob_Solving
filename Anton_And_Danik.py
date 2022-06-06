inp = input()
inp1 = input()
Acount = Dcount = 0 
for i in inp1:
    if(i=="A"):
        Acount+=1
    elif(i=="D"):
        Dcount+=1
if(Acount>Dcount):
    print("Anton")
elif(Dcount>Acount):
    print("Danik")
else:
    print("Friendship")