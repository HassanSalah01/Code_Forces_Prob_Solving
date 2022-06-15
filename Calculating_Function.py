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
