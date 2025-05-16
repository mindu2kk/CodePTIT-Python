"""
Nhập xâu ký tự S có độ dài không quá 100. Một từ được định nghĩa là một dãy ký tự không có khoảng trống.

Hãy tách xâu S thành các từ, mỗi từ in trên một dòng.

Input:

Chỉ có một dòng ghi xâu S (độ dài không quá 100)
"""

s = input()
res = s.split()
for char in res:
    print(char)