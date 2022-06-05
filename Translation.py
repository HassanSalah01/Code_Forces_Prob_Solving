y = ""
inp = input();
inp2=input();
for i in range(len(inp)-1,-1,-1):
    y+=inp[i];
if(inp2==y):
    print("yes")
else:
    print("No")