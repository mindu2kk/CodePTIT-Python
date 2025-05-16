"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số).

Output
Với mỗi bộ test, ghi ra kết quả tính được.
Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.
"""
def calc(n):
    res = 1
    for i in n:
        if i != "0":
            res *= int(i)
    return res

t = int(input())

for _ in range(t):
    n = input()
    print(calc(n))