def main():
    x =input()
    x = x.split(" ")
    for i in range(len(x)):
        x[i]=int(x[i])
    print(4-len(set((x))))


main()