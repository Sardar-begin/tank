n = int(input())
P = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)    
for r in P:
    a = [str(x) for x in r]
    print(' '.join(a))