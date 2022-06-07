def inp():
    x= input()
    y = x.split(" ")
    for i in range(len(y)):
        y[i]=int(y[i])
    return y

def main():
    count = 0 
    s = []
    x = int(input())
    for i in range(x):
        s = inp()
        if(s[0]!=s[1] and s[0]+2<=s[1]):
            count+=1
    print(count)

main()