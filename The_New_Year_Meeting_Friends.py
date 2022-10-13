def main():

    x = input().split(" ")
    for i in range(len(x)):
        x[i]= int(x[i])
    sum =int((x[1]-x[0])+(x[2]-x[1]))
    print(sum)

main()