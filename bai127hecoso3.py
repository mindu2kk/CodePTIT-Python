"""
Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.
Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

Input
Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

Output
Nếu đúng in ra YES, nếu sai in ra NO.
3
1214AB
10210221
22222222
"""
def test(s):
    for char in s:
        if char not in "012":
            return "NO"
    return "YES"
t = int(input())

for _ in range(t):
    s = input()
    print(test(s))