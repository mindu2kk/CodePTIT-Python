"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
Output:

Đưa ra kết quả mỗi test theo từng dòng.

2
12ab29cd19
ab123gh456cd
"""
n = int(input())

while n > 0:
    s = input()
    s += "*"
    res = 10 ** 19
    x = 0
    l = len(s)
    for i in range(0,l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = min(res,x)
                x = 0
    print(res)
    n -= 1