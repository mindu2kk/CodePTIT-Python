"""
Cho N số nguyên dương A[]. Mỗi lần, bạn chọn một tổ hợp gồm K số, như vậy, có tất cả C(K, N) cách chọn.
Bài toán đặt ra là hãy tính tổng của sự chênh lệch giữa số lớn nhất và nhỏ nhất trong tổ hợp được chọn của tất cả C(K, N) lần.

Input:
Dòng đầu tiên là số nguyên N và K (1 ≤ N ≤ 105, 1 ≤ K ≤ N).
Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 109).

Output:
In ra đáp án tìm được theo modulo 109+7.
"""

MOD = 10**9 + 7
def power(a,b,mod):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b //= 2
    return res

def preprocess(n,mod):
    fact = [1] * (n + 1)
    ifact = [1] * (n + 1)

    for i in range(2,n + 1):
        fact[i] = fact[i - 1] * i % mod
    ifact[n] = power(fact[n],mod - 2,mod)

    for i in range(n - 1,0,-1):
        ifact[i] = ifact[i + 1] * (i + 1) % mod
    ifact[0] = 1

    return fact,ifact

def comb(n,k,fact,ifact,mod):
    if n < k or k < 0:
        return 0
    return fact[n] * ifact[k] % mod * ifact[n - k] % mod

def solve(n,k,A):
    A.sort()
    fact,ifact = preprocess(n,MOD)
    result = 0

    for i in range(n):
        max_count = comb(i,k - 1,fact,ifact,MOD)
        min_count = comb(n - i - 1,k - 1,fact,ifact,MOD)
        result = (result + A[i] * (max_count - min_count) % MOD) % MOD
    print(result)
n,k = map(int,input().split())
A = list(map(int,input().split()))
solve(n,k,A)

