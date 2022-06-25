
def main():
    x =input()
    arr = []
    for i in x :
        if(i!="{" and i!="}" and i!="," and i!=" "):
            arr.append(i)
    print(len(set(arr)))
main()