def main():
    x = int(input())
    for i in range(x):
        x = int(input())
        y = 0 
        if(x<=2):
            y = 0
        elif(x%2==0):
            y = (x/2)-1
        else:
            x+=1
            y = (x/2)-1
        print(int(y))
main()