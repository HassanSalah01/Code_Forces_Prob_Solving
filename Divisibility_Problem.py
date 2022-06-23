def div(x,y):
    count = 0
    while(x%y!=0):
        count+=1
        x+=1
    return count

def div(x,y):
    count = 0 
    for i in range(1,9):
        if(x%(y*i)==0 and y*i>x):
            print(i)
            count = (y*i)-x
            break
        else:
            x+=1
        print(x)
    return count


