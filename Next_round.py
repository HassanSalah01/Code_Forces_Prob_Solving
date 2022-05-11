arr = []
inp1 = []
inp2=[]
x = input()
y = input()
x = x.split()
y = y.split()
for i in x:
    inp1.append(int(i))
for i in y:
    inp2.append(int(i))
for i in inp2:
    if(i >=inp2[(inp1[1]-1)] and i >0 ):
        arr.append(i)
print(len(arr))






