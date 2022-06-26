def pang(x):
    arr = []
    for i in x:
        arr.append(i)
    if(len(set(arr))>=26):
        return "Yes"
    else:
        return "NO"

def main():
    x =int(input())
    y= input()
    y = y.lower()
    if(x<26):
        print("NO")
    else:
        print(pang(y))
main()