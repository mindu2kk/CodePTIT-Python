"""
Cho dãy số A[] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A[].
Các tổ hợp cần liệt kê theo thứ tự từ điển (tức là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn, và tổ hợp sau lớn hơn tổ hợp trước).
Input

Dòng đầu ghi hai số N và K.
Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.
Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.

Output
Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.

8 3
2 4 4 3 5 1 3 4
"""
from itertools import combinations, permutations

n,k = map(int,input().split())
A = list(map(int,input().split()))

A = sorted(set(A))

for combi in permutations(A):
    print(*combi)