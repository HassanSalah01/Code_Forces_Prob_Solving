def main():
    size = int(input())
    inp = input()
    inp = inp.split(" ")
    for i in range(len(inp)):
        inp[i]=int(inp[i])
    police  =0 
    crime = 0 
    unsolved = 0
    for i in inp:
        if(i !=-1):
            police+=i
        elif(i==-1 and police-1<0 ):
            unsolved+=1
        else:
            police-=1

    print(unsolved)



main()