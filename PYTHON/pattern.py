# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #         print("*" ,end="")
# #     print("")

# # n=5
# # for i in range(n):
# #     s=" "
# #     for j in range(n):
# #         s+="*"
# #     print(s)

# # n=5
# # for i in range(n):
# #     s=""
# #     for j in range(n-i):
# #        s+="*"
# #     print(s)
n=5
# # for i in range(n):
# #     s=""
# #     for j in range(n-1-i):
# #         s+=" "
# #     for k in range(i+1):
# #         s+="*"
# #     print(s)

# # for i in range(n):
# #     s=" "
# #     for j in range(n-i-1):
# #         s+=" "
# #     for k in range(2*i+1):
# #         s+="*"
# #     print(s)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#     #     print(j,end="")
#     # print("")
# for i in range(n):
#     a=" "
#     for j in range(n):
#         a=i+1          
#         print(a) 

# n=5
# for i in range(0,n):
#     sum=" "
#     for j in range(1,n+1):
#         i+=1
#         sum+=str(i)
#         sum+=" "
#     print(sum)
        
# n=5
# for i in range(0,n):
#         sum=" "
#         for j in range(1,n+1):
#             i+=1
#             if(i<n+1):
#                 sum+=str(i)
#                 sum+=" "
#         print(sum)

# n=4 
# for i  in range(0,7):
#     k=" "
#     for j in range((2*n)-1):
#         top=i
#         bottom=j
#         left=(2*n-2)-i
#         right=(2*n-2)-i
#         k+=str(n-min(min(top,right),min(left,bottom)))
#     print(k)
        
# n=5
# for i in range(n):
#     s=" "
#     for j in range(n-i-1):
#         s+=" "
#         for k in range(1,i+1):
#             s+=str(i)
#         print(s)

for i in range(1,n+1):
    s=" "
    for j in range(1,i+1):
        s+=str(i)
    print(s)