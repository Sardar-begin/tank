n = int(input())

P = []
if n == 0:
    P.append([1])
if n == 1:
    P.append([1, 1])
else:
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1] + P[i-1][j]

        P(row) 
for r in P:
    print(r)
               

