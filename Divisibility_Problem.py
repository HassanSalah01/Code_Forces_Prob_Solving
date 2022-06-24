x = 123
y = 456


def div(x,y):
    f = x
    s = y
    t = 0
    q=2 
    while(x%y!=0 and q < y ):
        t = y*q
        q+=1
        if(t%y==0 and t > f):
            return t-x
    return 0

print(div)
def main():
    x =int(input())
    while(x>=0):
        inp = input()
        s = inp.split(" ")
        print(div(int(s[0]),int(s[1])))
