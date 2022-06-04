x = input().split(" ")
x = int(x[1])
line =input()
arr = []

for i in line:
    arr.append(i)

def swap(arr,i1,i2):
    temp = arr[i1]
    arr[i1]= arr[i2]
    arr[i2] = temp

while(x>0):
    ind = [];
    for i in range(0,len(arr)-1):
        if(arr[i]=="B" and arr[i+1]=="G"):
            ind.append(i)
    if(len(ind)>0):
        for i in ind:
            swap(arr,i,i+1)
    x-=1
    
fin  = '';
for i in arr:
    fin+=i
print(fin)






