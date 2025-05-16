"""
Mảng a ban đầu có n số nguyên. Bạn có thể thực hiện thao tác sau nhiều lần:
            - Chọn số 2 số x và y bất kỳ trong mảng và thêm 2x – y vào mảng.
Với 1 số nguyên k, hãy kiểm tra xem bạn có thể tạo ra được số k hay không.

Input:
Dòng đầu tiên chứa số bộ test t (t ≤ 20).
Mỗi test có định dạng như sau:
            - Dòng đầu tiên chứa 2 số nguyên n và k (2 ≤ n ≤ 105, -109 ≤ k ≤ 109)
            - Dòng tiếp theo chứa n số nguyên ban đầu (-109 ≤ ai ≤ 109)

Output:
Với mỗi test, in ra “YES” nếu có thể và “NO” trong trường hợp còn lại.
"""
from math import gcd

def tinh(A,n,k):
    base = A[0]
    g = 0
    A.sort()
    for i in range(1,n):
        g = gcd(g,A[i] - base)

    return "YES" if (k - base) % g == 0 else "NO"
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))

    print(tinh(A,n,k))
