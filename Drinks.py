def main():
    arr = []
    s = 0
    x = int(input())
    y = input()
    y = y.split(" ")
    for i in range(len(y)):
        s+=int(y[i])
    print(s/x)


main()