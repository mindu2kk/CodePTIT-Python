"""

6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
"""
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def check(n,m,matrix):
    min = 1000000
    max = -1
    for row in matrix:
        for col in row:
            if col < min:
                min = col
            if col > max:
                max = col
    return min,max

min_val, max_val = check(n, m, matrix)
ans = max_val - min_val
ok = 0
res = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == ans:
            res.append((i,j))
            ok = 1
if ok == 0:
    print("NOT FOUND")
else:
    print(ans)
    for i,j in res:
        print(f"Vi tri [{i}][{j}]")



