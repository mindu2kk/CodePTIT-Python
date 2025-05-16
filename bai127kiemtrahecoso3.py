"""
Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.
Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

Input
Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

Output
Nếu đúng in ra YES, nếu sai in ra NO.
"""

t = int(input())

for _ in range(t):
    s = input()
    print("YES" if all(char in '012' for char in s) else "NO")