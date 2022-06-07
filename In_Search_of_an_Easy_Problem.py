def inp():
    x= input()
    y = x.split(" ")
    for i in range(len(y)):
        y[i]=int(y[i])
    return y

def main():
    y = []
    count = 0
    x = int(input())
    y = inp()
    for i in y:
        if (i!=0):
            count+=1
    if(count):
        print("HARD")
    else:
        print("EASY")

main()