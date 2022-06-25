def div(x,y):
    if(x%y!=0):
        return y-(x%y)
    else:
        return 0
def main():
    x =int(input())
    arr = []
    while(x>0):
        inp = input()
        s = inp.split(" ")
        arr.append(div(int(s[0]),int(s[1])))
        x-=1
    for i in arr:
        print(i)
    
main()