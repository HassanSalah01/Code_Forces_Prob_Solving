def main():
    numb = int(input())
    arr = []    
    count = 1
    for i in range(numb):
        arr.append(int(input()))

    for i in range(len(arr)-1):
        if (arr[i]!=arr[i+1]):
            count+=1
    return count


main()


