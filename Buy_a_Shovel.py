def main():
    all = input().split(" ")
    x = int(all[0])
    y = int(all[1])
    sum = x

    while((sum%10)-y!=0 or (sum%10)!=0):
        if((sum%10)-y==0 or (sum%10)==0):
            print(int(sum/x))
            return int(sum/x)
        sum+=x
    
    
main()