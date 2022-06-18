def minMax(x):
    min = x[0]
    max = x[0]
    for i in x:
        if(i > max):
            max = i
        elif(i <=min):
            min = i
    return [min,max]

def ind(arr,x,t):
    ind = 0
    for i in range(len(arr)):
        if(arr[i]==x and t==1):
            ind = i
        if(arr[i]==x and t==0):
            ind = i
            break

    return ind

def sol(arr,min , max):
    mi = ind(arr,min,1)
    ma = ind(arr,max,0)
    cal = len(arr)-mi-1
    cal2 = ma-0
    if(mi<ma):
        return cal+cal2-1
    else:
        return cal+cal2


def main():
    x = input()
    y = input()
    y = y.split(" ")
    for i in range(len(y)):
        y[i]=int(y[i])
    sss = minMax(y);
    print(sol(y,sss[0],sss[1]));


main()










 
