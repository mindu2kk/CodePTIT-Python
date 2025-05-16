"""
Nhập xâu s1, giả sử gọi xâu đảo là s2. Hãy kiểm tra xem khoảng cách ký tự cạnh nhau trong hai xâu có thỏa mãn công thức sau hay không:
|s1[i] – s1[i-1]| = |s2[i] – s2[i-1]| với tất cả giá trị 0 < i < N

Input
Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

Output
Ghi ra YES hoặc NO.
2
acxz
bcxz
"""

def check(s):
    n = len(s)
    rev = s[::-1]

    for i in range(1,n):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    s = input().strip()
    print(check(s))