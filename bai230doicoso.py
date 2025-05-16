"""
Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).
Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test ghi 2 số N và b.
Nlà một số nguyên dương N trong cơ số 10, không quá 100.000.  2 ≤ b ≤ 36

Output
Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.

3
10 2
2021 2
31 16
"""
def change_base(n,b):
    char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = ""
    while n > 0:
        base = n % b
        res = char[base] + res
        n //= b
    return res

t = int(input())

for _ in range(t):
    n,b = map(int,input().split())
    print(change_base(n,b))



