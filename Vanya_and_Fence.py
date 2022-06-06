def inp():
    x= input()
    y = x.split(" ")
    for i in range(len(y)):
        y[i]=int(y[i])
    return y
def solution():
    x = inp()
    y = inp()
    count = 0
    for i in y:
        if(i > x[1]):
            count+=2
        else:
            count+=1  
    return count
def main():
    print(solution())
    
main()
