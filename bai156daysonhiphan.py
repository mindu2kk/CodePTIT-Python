 """
Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.
Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

Input
Dòng 1 ghi số N là số phần tử của dãy (không quá 100).
Dòng 2 ghi N số nhị phân.

Output
Ghi ra kết quả bài toán.
"""

n = int(input())

A = list(map(int,input().split()))
cnt = 0
for i in range(n - 1):
    if A[i] != A[i + 1]:
       cnt += 1
print(cnt)