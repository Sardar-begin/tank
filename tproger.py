# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # for elem in a:
# #     if elem < 5:
# #         print(elem)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# def selection_(a,b):
#     # out = list(filter(lambda it: it in a,b))
#     # return out
#     c = []
#     for i in a:
#         for j in b:
#             if i == j and i not in c:
#                 c.append(i)
#     return c


# print(selection(a,b))



# n = int(input())
# s = 0
# for i in range(n+1):
#   s = s+i*i
# print("s =", s)

# l = list("hello")
# print(l)

# n = int(input())
# k = n // 3600
# n = n % 3600
# p = n // 60
# n % 60
# print(k,"час", p,'minut', n, 'sec')

# a = int(input())
# b = int(input())
# if a > b:
#   print(a, "больше", b)
# else:
#     print(a, "меньше", b)  

# n = int(input())
# for i in range(0,10):
#   print(n, end=" ")

# i = 0
# while i < 10:
#       print(20, end=" ")
#       i = i + 1      
# a = int(input())
# if a < 50:      
#   for i in range(a,51):
#     print(i)
# else:
#   print('vvedite menshe') 

# a = int(input())
# b = int(input())
# if b >= a:
#       for i in range(a,b):
#             print(i)
# else:
#     print("не выполнимо")

# for i in range(10,26):
#     print(i, i+0.4)

# for i in range(25,35):
#     print(i, i+0.5, i-0.2)

# i = 25
# while i < 35:
#   print(i, i+0.5, i-0.2)
#   i = i + 1  

# a = 20.4
# for i in range(2,21):
#   print(i, "-", a)

# a = 2.54
# for i in range(10,23):
#   print(i * a, "см" )

# d = 2.54
# i = 10
# while i < 22:
#   print(i * d, "см" )
#   i = i + 1

# from random import randint

# N = 10
# a = []
# for i in range(N):
#     a.append(randint(1, 200))
# print(a)


# for i in range(N-1):
#     for j in range(N-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]

# print(a)
