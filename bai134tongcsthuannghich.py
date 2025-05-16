"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.

Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

22222222222222222222
"""


def test(n):
    tong = sum(int(digit) for digit in n)
    if str(tong) == str(tong)[::-1] and tong > 10:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = input()
    print(test(n))