def main():
    x = int(input())
    arr = [100,20,10,5,1]
    count = 0
    for i in arr:
        if(x>=i and x!=0):
            count+=(x-(x%i))/i
            x=x%i
        else:
            continue
    print(int(count))
main()
