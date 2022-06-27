x = 1000000000
def main():
    x = int(input())
    arr = [100,20,10,5,1]
    count = 0
    for i in arr:
        while(x>=i):
            x-=i
            count+=1
    print(count)
main()




# x = 125
# arr = [100,20,10,5,1]
# t = 0 
# s = arr[t]
# count = 0 
# while(x and len(arr)>t):
#     print(x,t,s,count)
#     if(x%s<s):
#         if(x>s):
#             print("s")
#             x = x%s
#             t+=1
#             s = arr[t]
#             count+=1
#     else:
#         t+=1
#         s = arr[t]

# print(count)