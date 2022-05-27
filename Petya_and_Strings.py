x = input().lower()
y = input().lower()
sort = 0;
for i in range(len(x)):
        if(x[i]>y[i]):
            sort = 1
            break
        elif(x[i]<y[i]):
            sort = -1
            break
print(sort)

