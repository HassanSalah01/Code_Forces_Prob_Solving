x = int(input())
sub = ["love","hate"]
ver = ["that ","it"]
wor = ""
t = 1

while(x>0):
    if(t):
        wor+=f"I {sub[1]} "
    else:
        wor+=f"I {sub[0]} "
    if(x!=1):
        wor+=ver[0]
    else:
        wor+=ver[1]
    t =not t
    x-=1
print(wor)
