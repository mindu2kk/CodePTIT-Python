"""
Hệ thống máy tính mới chuyển sang sử dụng hệ đếm tam phân với ba chữ số 0, 1, 2.
Do vốn đã quen với hệ đếm nhị phân nên Nam chỉ quan tâm đến các số tam phân thỏa mãn chữ số 2 chiếm ưu thế,
tức là số lượng chữ số 2 chiếm nhiều hơn 50% số chữ số của số đó.
Hãy giúp Nam liệt kê N số tam phân mà số 2 chiếm ưu thế đầu tiên (theo thứ tự từ nhỏ đến lớn).

Input
Dòng đầu ghi số bộ test (không quá 20)
Mỗi bộ test ghi số nguyên dương N (không quá 1000)

Output
Với mỗi test, viết trên một dòng N số tam phân ưu thế 2, các số cách nhau một khoảng trống.
"""
def covert(n):
    res = ""
    if n == 0:
        return "0"
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

def check(res):
    cnt2 = res.count('2')
    return cnt2 > len(res) / 2

def test(n):
    so = 1
    res = []
    while len(res) < n:
        coso3 = covert(so)
        if check(coso3):
            res.append(coso3)
        so += 1
    return " ".join(res)


t = int(input())

for _ in range(t):
    n = int(input())
    print(test(n))
