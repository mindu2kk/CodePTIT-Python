"""
Một xâu ký tự được gọi là “thăng bằng” nếu khoảng cách của tất cả các cặp ký tự cạnh nhau trong xâu đó đều đúng bằng khoảng cách
của hai vị trí tương ứng trong xâu đảo của nó.
Ví dụ xâu s1 có độ dài N và xâu đảo của nó là s2 thì xâu này sẽ thỏa mãn tính chất thăng bằng nếu:
|s1[i] – s1[i-1]| = |s2[i] – s2[i-1]| với tất cả giá trị 0 < i < N
Hãy kiểm tra xem một xâu ký tự bất kỳ có phải là xâu “thăng bằng” hay không.

Input
Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

Output
Ghi ra YES hoặc NO.
"""
def test(n):
    rev = n[::-1]
    l = len(n)
    for i in range(1,l):
        if abs(ord(n[i]) - ord(n[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = input()
    print(test(n))