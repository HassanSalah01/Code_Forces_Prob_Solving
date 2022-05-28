str = input()
arr = str.split('+')
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)):
    ind = 0;
    min = arr[i]
    for j in range(i,len(arr)):
        if(arr[j]<=min):
            min = arr[j]
            ind = j
    arr[ind]=arr[i]
    arr[i]=min
fin = ''
for i in arr:
    fin+=f"{i}+"
print(fin[:-1])