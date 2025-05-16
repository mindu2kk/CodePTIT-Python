"""
Cho hai xâu ký tự s1 và s2. Xâu s2 được gọi là một “sắp đặt lại” của xâu s1 nếu tập ký tự của xâu s2 hoàn toàn giống
với xâu ký tự s1, tính cả số lần xuất hiện của từng ký tự.
Ví dụ: s2 = “intestg” là sắp đặt lại của xâu “testing”
Còn xâu “aabbbcccc” không được coi là sắp đặt lại của xâu “abc”.
Nhập 2 xâu s1 và s2 có độ dài không quá 1000 ký tự, chỉ bao gồm các ký tự viết thường, không có khoảng trống.
Hãy kiểm tra xem s2 có phải là sắp đặt lại của s1 hay không.

Input
Dòng đầu ghi số bộ test, không quá 5000.
Mỗi test ghi trên 2 dòng lần lượt là xâu s1 và s2.

Output
Ghi ra thứ tự bộ test, sau đó là YES hoặc NO tùy thuộc kết quả kiểm tra.
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
"""
from collections import Counter

t = int(input())

for i in range(1,t + 1):

    s1 = input().strip()
    s2 = input().strip()
    if Counter(s1) == Counter(s2):
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")