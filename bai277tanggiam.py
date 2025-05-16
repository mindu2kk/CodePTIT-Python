"""
Cho hai dãy số thực A[] và B[] đều có N phần tử, các giá trị là số thực và không quá 100.
Hãy tính độ dài dài nhất của dãy các vị trí (không cần liên tiếp) thỏa mãn cả hai điều kiện:
Nếu xét các vị trí đó trên dãy A[] thì dãy con thu được thỏa mãn tính chất tăng dần (giá trị bằng nhau không được tính vào dãy tăng).
Nếu xét các vị trí đó trên dãy B[] thì dãy con thu được thỏa mãn tính chất giảm dần (giá trị bằng nhau không được tính vào dãy giảm).

Input
Dòng đầu ghi số bộ test (không quá 100).
Mỗi bộ test bắt đầu bởi số N (không quá 500).
Tiếp theo là N dòng, mỗi dòng ghi 2 giá trị A[i] và B[i]

Output
Với mỗi test, ghi ra độ dài tính được trên một dòng.

3
2
1.0 1.0
1.5 0.0
3
1.0 1.0
1.0 1.0
1.0 1.0
6
1.5 9.0
2.0 2.0
2.5 6.0
3.0 5.0
4.0 2.0
10.0 5.5
"""
def longest(n,arr):
    dp = [1] * (n + 1)
    for i in range(n):
        for j in range(i):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [tuple(map(float,input().split())) for _ in range(n)]
    print(longest(n,arr))