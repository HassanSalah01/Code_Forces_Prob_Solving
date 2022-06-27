def inp():
    arr = []
    arr2=[]
    x = int(input())
    for i in range(x) :
        y = input()
        y=y.split(" ")
        arr.append(int(y[0]))
        arr2.append(int(y[1]))
    return [arr,arr2]

def main():
    x = inp()
    arr =x[0]
    arr2 = x[1]
    count = 0 
    for i in arr:
        for j in arr2:
            if(i == j):
                count+=1
    print(count)


main()