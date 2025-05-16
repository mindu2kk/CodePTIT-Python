"""
Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển và nối với tổng các chữ số trong S ở cuối cùng. Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.

Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test là một xâu ký tự S.
T, S thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ Length(S)≤105.

Output:
Đưa ra kết quả mỗi test theo từng dòng.

2
AC2BEW3
ACCBA10D2EW30
"""

t = int(input())

for _ in range(t):
    s = input()
    tong = sum(int(i) for i in s if i.isdigit())
    res = ""
    s = sorted(s)
    for c in s:
        if c.isalpha():
            res += c
    res += str(tong)
    print(res)

