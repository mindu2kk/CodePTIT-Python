"""
Cho dãy số nguyên x1 , x2 , … ,x  và số nguyên m
- Tìm giá trị lớn nhất của dãy số.
- Chèn m vào trước vị trí đầu tiên có giá trị bằng giá trị lớn nhất.
- Sắp xếp lại dãy số sau chèn sao cho phần tử âm về đầu dãy, phần tử dương và bằng 0 về cuối dãy sao cho trật tự các phần tử không thay đổi.

Input:
Dòng đầu tiên cho T là số lượng bộ test.
Mỗi bộ test bao gồm hai dòng, dòng 1 cho số n < 1000 là số lượng phần tử và số m sao cho  -109 < m < 109.
Dòng thứ 2 của bộ test bao gồm m số nguyên -109 < Xi < 109

Output:
In ra kết quả theo từng dòng

1
5 3
-1 2 3 4 -1
"""

t = int(input())
def test(n,m,A):
    res = []
    max_val = max(A)

    for i in range(n):
        if A[i] == max_val:
            A.insert(i,m)
            break

    negative = [x for x in A if x < 0]
    positive = [x for x in A if x >= 0]

    res = negative + positive
    print(*res)

for _ in range(t):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    test(n,m,A)