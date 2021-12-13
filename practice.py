# list1 = [8, 19, 148, 4]  
# list2 = [9, 1, 33, 83]
# result1 = []
# result2 = []
# for i in list1:
#     for j in list2:
#         result1.append(i * j)
# print(result1)

# for k, i in enumerate(list1):
#     result2.append(i * list2[k])

# print(result2)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in l:
#     for k in range(2, 10):
#         print(f'{i} * {k} = {i * k}')

# print('hello', 'melllo')

# n = 3
# m = 4
# a = [[0]*m for i in range(n)]
# print(a, end = ' ')
# print(len(a))

N, M = map (int, input ().split ())

matrix = []
x = 0
for i in range(N):
    tmp = []
    for j in range(x, M+x):
        tmp.append(j)
    x += 1
    matrix.append(tmp)
print(matrix[0][0], matrix[0][-1], matrix[-1][-1], matrix[-1][0])


