# list = [1,2,3,4,5,6,7]


# # Find an element in a list
# def find(list,number):
#     for i in range(1,len(list)+1):
#         if i == number:
#             print("found")
#         else:
#             print("not found")

# find(list,1)

# Print items in a range  ---- time complexity O(n)

# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)

# #Print items with nested for loops ---- time complexity O(n²)  n * n  ( 3 times 3 = 9 ) 9 operations
# # Triple for loop nested is a n * n * n --> n³ (n cubed)   -> n²

# def print_items2(n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)


# print_items2(3)


# Drop Non-dominants In this case we have a O(n²) + O(n)  > So drop the O(n) hence we got only O(n²)

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)

#     for k in range(n):
#         print(k)

# Constant time O(1)

def sum(n):
    return n + n + n + n + n + n 

print(sum(9999))


#print_items(3)