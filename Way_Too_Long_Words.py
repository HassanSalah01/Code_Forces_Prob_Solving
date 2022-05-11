x = int(input())
arr = []
for i in range(x):
    arr.append(input())
for i in arr:
    if(len(i)>10):
        print(f"{i[0]}{len(i)-2}{i[-1]}")
    else:
        print(i)
