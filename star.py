# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end="")
#     print()

#1 for i in range(1,6):
#     for j in range(1,i):
#         print("*",end="")
#     print()

#2 for i in range(1,5):
#     for j in range(1,5):
#         if i>=j :
#             print("*",end="")
#     print()

m=int(input("Enter a row:"))
n=int(input("Enter a column:"))
for i in range(0,m):
    for j in range(0,n):
        if i==0 or i==m-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()