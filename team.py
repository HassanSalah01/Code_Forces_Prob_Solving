x = int(input())
arr = []
for i in range(x):
    arr.append(input())
count = 0
for i in arr:
    if("1 1"in i or "1 0 1" in i):
        count+=1
print(count)

