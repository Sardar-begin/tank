from random import randint
n = int(input())
mas = []
for i in range(n):
    mas.append(randint(1,100))

for run in range(n-1):    
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            mas[i],mas[i+1] = mas[i+1],mas[i]
print(mas)
print(mas[0], mas[-1])
print(min(mas))
print(max(mas))
# n = 5
# mas = [12, 4, 1, 3, 9]

# i = 0

# while i < n:
#     j = 0
#     while j < n-1:
#         if mas[j+1] < mas[j]:
#             mas[j], mas[j+1] = mas[j+1], mas[j]
#         j = j + 1
#     i = i + 1 
# print(mas)

