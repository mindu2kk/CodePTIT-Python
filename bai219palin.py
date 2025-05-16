"""
Số tự nhiên x được gọi là palindrome (đối xứng) trong hệ đếm a nếu viết xuôi hay ngược
đều cho cùng một kết quả.
Số tự nhiên x được gọi là song đối xứng a, b nếu x là palindrome đồng thời trong
cả hai hệ đếm a và b. Cho số nguyên không âm x và hai hệ đếm a và b.
Hãy hiển thị YES nếu x là số song đối xứng trong cả hai hệ đếm a và b, ngược lại, hiển thị NO.

Input: mỗi dòng 3 số x, a, b. Kết thúc input là -1.
Giới hạn: 0 £ x £ 55000000, 2 £ a, b £ 20

0 2 10
11 2 10
6 7 16
-1
"""

def to_base(x, base):
    if x == 0:
        return "0"
    res = ""
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res

def is_palindrome(s):
    return s == s[::-1]

while True:
    s = input()
    if s == '-1':
        break
    x, a, b = map(int, s.split())

    if is_palindrome(to_base(x, a)) and is_palindrome(to_base(x, b)):
        print("YES")
    else:
        print("NO")
