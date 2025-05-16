"""
Nhập số nguyên dương N (1 < N < 10000).

Viết chương trình tính tổng:

S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
Kết quả được in ra với 6 chữ số phần thập phân.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi test ghi một số N

Output
Với mỗi bộ test, ghi ra kết quả trên một dòng
"""
def calc(n):
    s = 0.0
    if n % 2 == 1:
        for i in range (1,n + 1,2):
            s += 1 / i
    else:
        for i in range (2,n + 1,2):
            s += 1 / i
    return s
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    ans = calc(n)
    print(f"{ans:.6f}")
