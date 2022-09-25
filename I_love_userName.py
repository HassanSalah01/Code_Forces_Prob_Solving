# 100 50 200 150 200

def main():
    x = int(input())
    y = input().split(" ")
    max= min = int(y[0])
    count = 0 
    y = list(map(int, y))
    for i in y:
        if(int(i) < min):
            min = i
            count+=1
        elif(int(i) > max):
            max = i
            count+=1
    print(count)



main()