def isEqual(x,y):
    return x==y

def moves(x,y):
    res = min(x,y)
    count = 0 
    if(res==y):
        res = x-y
    else:
        res = y-x
    if(res%10==0):
        count = res/10
    elif(res%10!=0):
        count= (int(res/10))
        count+=1
    print(int(count))


def main():
    inpLength = int(input())
    for i in range(inpLength):
        arr = input().split(" ")
        x = int(arr[0])
        y=int(arr[1])
        if(isEqual(x,y)):
            print(0)
        else:
            moves(x,y)
            



main()