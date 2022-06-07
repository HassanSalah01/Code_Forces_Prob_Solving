def inp():
    x= input()
    y = x.split(" ")
    for i in range(len(y)):
        y[i]=int(y[i])
    return y

