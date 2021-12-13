# st = input()
# it = 0
# res = []
# for i in range(2, len(st), 2):
#     if st[i] != st[i-2]:
#         res.append(st[it:i].split())
#         it
#  = i
# res.append(st[it:].split())
# print(res)

# n = list(map(int, input().split()))
# temp = []
# result = []

# for i in temp:
#     if len(temp) == n:
#          temp.append()

#   

# n = 5
# a = [[19, 21, 33, 78, 99], 
#      [41, 53, 66, 98, 76], 
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]

# maximum = -1
# minimum = 100

# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)

# members = [['3', '5', '5', '20', 'D'], ['2', '2', '2', '30', 'C']]
# for item in members:
#     print(' '.join(item))

rows = int(input())
cols = int(input())
n = rows * cols

matrix = []
arr = []
for i in range(rows):
    arr.append([str(input()) for _ in range(cols)])

# print(arr)

for x in range(rows):
   for j in range(cols):
       print(arr[x][j], end=' ')

print()

for x in range(rows):
   for j in range(cols):
       print(arr[x][j], end=' ')

# x = [1,2,3,4,5]

# new = [i**2 for i in x]

# # new = []
# # for i in x:
#     # new.append(i**2)

# print(new)