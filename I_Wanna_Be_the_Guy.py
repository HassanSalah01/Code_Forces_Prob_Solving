def inp():
    x= input()
    y = x.split(" ")
    arr = []
    for i in range(len(y)):
        if(y[i]=="0" or i==0):
            continue
        else:
            arr.append(int(y[i]))
    return arr
def main():
    x = int(input())
    arr = inp()
    arr2 =inp()
    if(len(set((arr+arr2)))==x):
        print("I become the guy.")
    else:
        print( "Oh, my keyboard!" )
main()