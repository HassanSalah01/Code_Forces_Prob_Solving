def solution(arr):
    arr.sort()
    arrLen = len(arr)-2
    while(len(arr)>1):
        x = arr.pop()
        if(abs(x-(arr[arrLen]))>1):
            print("No")
            return 
        arrLen-=1
    print("Yes")


def main():
    x = int(input())
    for i in range(x):
        x = input()
        x=input().split(" ")
        for i in range(len(x)):
            x[i]=int(x[i])
        solution(x)



main()