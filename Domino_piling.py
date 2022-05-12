x = input()
x=x.split()
count = 0
z = (int(x[0])*int(x[1]))
while(z>1):
    z-=2
    count+=1
print(count)
