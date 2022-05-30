x =input()
x= x.split(" ");
numb = int(x[0])
count = int(x[1])
while(count>0):
    if(numb%10==0):
        numb/=10
    else:
        numb-=1
    count-=1

print(int(numb))

