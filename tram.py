x = int(input())
total = 0;
max = 0 ;
while(x>0):
    f = input().split(" ")
    total-=int(f[0])
    total+=int(f[1])
    if(total > max):
        max = total
    x-=1
print(max)
