def main():
    x = input()
    y = input()
    s = ""
    for i in range(len(x)):
        t=int(x[i]) ^ int(y[i])
        s+=str(t)
    print(s)

main()
