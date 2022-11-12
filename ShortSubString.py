def subString(str):
    str2 = ""
    str2 +=str[0]
    for i in range(1,len(str),2):
        str2+=str[i]
    print(str2)

def main():
    x = int(input())
    while(x):
        inp =input()
        subString(inp)
        x-=1

main()