from random import randint
#n = 8
# a = list(map(int, input().split()))

#a = [randint(1,100) for i in range(n)]

a = [2, 1, 10, 50, 10]
n = len(a)
for run in range(n-1):
    for i in range(n-1):
        if a[i] < a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a) 

sum = 0
m = 0
d = n%2
r = round(n/2)
print(d,r)
if d > 0:
  m = r + 1
else:
  m = r 
print(m)
for k in range(m):
    sum += a[k]
print(sum)            


т 