def main ():
    socks = input().split(" ")
    color1 = max(int(socks[0]),int(socks[1]))
    color2 = min(int(socks[0]),int(socks[1]))
    result = []
    if(color1 == color2):
        print(color1,0)
    else:    
        result.append(color2)
        result.append((color1-color2))
        if(result[1]%2==0):
            print(result[0],int(result[1]/2))
        elif(result[1]<=1):
            print(result[0],0)
        else:
            print(result[0],int((result[1]-(result[1]%2))/2))

main()