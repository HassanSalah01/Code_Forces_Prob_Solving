



# def main():
#     arr = [1,1,1,0,1,1]
#     stk = []
#     top = -1
#     count=0
#     i = 0
#     while(i<len(arr)-1):
#         print(i,top,arr[i],arr[i+1],count)
#         if(top==-1 and arr[i]!=arr[i+1]):
#             print("ifff",1)
#             top+=1
#             stk.append(arr[i])
#         elif(top!=-1 and stk[top]!=arr[i]):
#             print("ifff",2)
#             top+=1
#             stk.append(arr[i])
#         elif (top !=-1 and stk[top]==arr[i]):
#             print("ifff",3)
#             i-=2
#             count +=(top+1)
#             stk = []
#             top = -1  
#         i+=1
#     if(arr[len(arr)-2] !=arr[len(arr)-1]):
#         count+=2
#     print("test",count)

# main()
# for i in range(len(arr)-1):
#     print(i)
#     if(top==-1):
#         push(arr[i])
#     elif(arr[i]==stk[top] and top == 0):
#         pop()
#         push(i)
#     elif(arr[i]!=stk[top]):
#         push(i)
#     elif(top==0):
#         top =-1
#     else:
#         count+=top+1
#         top = -1

# print(count)


# for i in range(len(arr)-1):
#     if(top==-1 and arr[i]!=arr[i+1]):
#         push(arr[i])
#     if(stk[top]!=arr[i]):
#         push(arr[i])
#     else:
#         count+=top+1
#         top = -1


# def inpt():
#     y = int(input())
#     x = []
#     for i in range(y):
#         x.append(int(input()))
#     return x
# def newArr(x):
#     arr = []
#     for i in range(len(x)-1):
#         if(x[i]!=x[i+1]):
#             arr.append(x[i])
#         else:
            
#             arr.append("*")
#     if(x[len(x)-1]!=x[len(x)-2]):
#         arr.append(x[i])
#     else:
        
#         arr.append("*") 
#     print(arr)
# def main():
#     # arr = inpt();
#     # print(arr)
#     newArr([1,10,1,1,1])
        

# main()