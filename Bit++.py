x = int(input())
arr = []
count = 0
for i in range(x):
    arr.append(input())
for i in arr:
    if("++"in i):
        count+=1
    elif("--"in i):
        count-=1
print(count)