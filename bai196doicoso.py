"""
Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).
Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test ghi 2 số N và b.
Nlà một số nguyên dương N trong cơ số 10, không quá 100.000.  2 ≤ b ≤ 36

Output
Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.
"""
def test(N,b):
    char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while N > 0:
        res = char[N % b] + res
        N //= b
    return res

t = int(input())

for _ in range(t):
    N,b = map(int,input().split())
    print(test(N,b))