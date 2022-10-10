def count (x):
    arr = []
    y=0
    for i in range(len(x)-1,-1,-1):
        if(x[y][0]=="0"):
            y+=1
        else:
            arr.append(x[y]+"0"*i)
            y+=1
    strs =""
    print(len(arr))
    for s in arr :
        if(s[0]!="0"):
            strs+=s
            strs+=" "
    print(strs)


def main():
    inp = int(input())
    for i in range(inp):
        item = input()
        count(item)


main()