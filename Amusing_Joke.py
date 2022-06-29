from re import T


def main():
    x = input()
    y = input()
    s = input()
    count1 = 0 
    count2 = 0 
    if(len(x)+len(y)==len(s)):
        t = x+y
        for i in range(len(s)):
            count1+=ord(t[i])
            count2+=ord(s[i])
        if(count1==count2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
print(ord("A"))
print(ord("B"))
print(ord("C"))