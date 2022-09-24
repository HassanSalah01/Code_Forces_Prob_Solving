def main():
    line = x = input().split(" ")
    x = int(line[0])
    y = int(line[1])
    s = 1
    for i in range(int((x+1)/2)):
        print("#"*y)
        if(i!=int((x+1)/2)-1):
            if(s):
                print("."*(y-1)+"#")
                s = 0
            else:
                s = 1
                print("#"+"."*(y-1))

main()