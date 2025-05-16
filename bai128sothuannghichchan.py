"""
Cho số nguyên dương N không quá 6 chữ số.
Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:
N là số thuận nghịch
Tất cả các chữ số của N đều chẵn
Số chữ số của N cũng là một số chẵn

Input
Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

Output
Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.
    return sum(int(digit) for digit in str(s))

1 2 3 4 91 101 111 121 131 182 192 202 212 222 273 283
"""
def check(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

def test(n):
    res = []
    for l in range(2,7,2):
        dau = 10 ** (l // 2- 1)
        sau = 10 ** (l // 2)

        for i in range(dau,sau):
            half = str(i)
            palin = int(half + half[::-1])
            if palin >= int(n):
                break
            if(check(palin)):
                res.append(str(palin))
    return " ".join(res)

t = int(input())
for _ in range(t):
    n = input()
    print(test(n))