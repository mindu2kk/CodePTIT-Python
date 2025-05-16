"""
10
1 2 3 4 5 6 7 7 9 6
"""

n = int(input())
A = []
while len(A) < n:
    i = [int(x) for x in input().split()]
    A += i

even = sorted([x for x in A if x % 2 == 0])
odd = sorted([x for x in A if x % 2 == 1], reverse=True)

# Chỉ số để duyệt danh sách chẵn/lẻ đã sắp xếp
i_even, i_odd = 0, 0

# Xây dựng kết quả theo vị trí gốc
result = []
for x in A:
    if x % 2 == 0:
        result.append(even[i_even])
        i_even += 1
    else:
        result.append(odd[i_odd])
        i_odd += 1

# In kết quả
print(*result)
