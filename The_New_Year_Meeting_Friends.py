def diff(x,y) :
    if(x>y):
        return x-y
    else:
        return y-x

def main() :
    x = input().split(" ")
    for i in range(len(x)):
        x[i]= int(x[i])
    sum = 0
    for i in x:
        sum+=i
    sum = sum/len(x)
    sum2 = 0 
    for i in x :
        sum2 +=diff(i , sum)
    print(int(sum2))

main()