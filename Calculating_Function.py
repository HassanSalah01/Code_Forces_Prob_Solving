def IsEven(x):
    return x%2

def main():
    x = int(input())
    if(IsEven(x)):
        s = ((x*(x+1))/2)/x
        print(int(s*-1))
    else:
        print(int(((x*(x+1))/2)/x))

main()
# def main():
#     x = int(input())
#     if(IsEven(x)):
#         od =(x+1)/2
#         od= od**2
#         evn = (x-1)/2
#         evn = 2*(evn*(evn+1))/2
#     else:
#         od = x/2
#         od= od**2
#         evn = x/2
#         evn = 2*(evn*(evn+1))/2
#     print((od*-1)+evn)

# main()
# 
# 1000000001
# x = 11
# evn = (x-1)/2
# evn = 2*(evn*(evn+1))/2
# print(evn)

print(int(((3052460231*(3052460231+1))//2)//3052460231))
