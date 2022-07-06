
def main():
    name1 = input()
    name2 =input()
    name3=input() 
    name4 = name1+name2
    arr = []
    arr2= []
    sol = "YES"
    if(len(name1)+len(name2)==len(name3)):
        for i in name3:
            arr.append(i)
    for i in range(len(name3)):
        if(name4[i] in arr):
            x = arr.index(name4[i])
            arr[x] = "#"
    for i in arr:
        if(i!="#"):
            sol ="NO"
            break
    print(sol)
main()
# dictt = {
#     "a":1
# }

# print(dictt['b'])
# print(dictt)


# def main():
#     x = input()
#     y = input()
#     s = input()
#     count1 = 0 
#     count2 = 0 
#     if(len(x)+len(y)==len(s)):
#         t = x+y
#         for i in range(len(s)):
#             count1+=ord(t[i])
#             count2+=ord(s[i])
#         if(count1==count2):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")
# print(ord("A"))
# print(ord("B"))
# print(ord("C"))