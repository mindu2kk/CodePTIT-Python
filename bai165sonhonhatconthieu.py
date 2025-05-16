"""
Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.

Input
Dòng đầu ghi số N (1 <= N <= 30000).
Dòng tiếp theo ghi N số của dãy A (1 <= A[i] <= 30000).

Output
Ghi ra số nhỏ nhất còn thiếu nếu có.
(khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).
"""
def test(n,A):
    num_set = set(A)

    for nums in range(1,n + 1):
        if nums not in num_set:
            return nums
    return n + 1
n = int(input())
A = list(map(int,input().split()))
print(test(n,A))
