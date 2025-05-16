"""
Cho một phép toán có dạng a + b = c với a,b,c chỉ là các số nguyên dương có một chữ số.
Hãy kiểm tra xem phép toán đó có đúng hay không.

Input
Chỉ có một dòng ghi ra phép toán (gồm đúng 9 ký tự)

Ouput
Ghi ra YES nếu phép toán đó đúng. Ghi ra NO nếu sai.
"""

n = input()
a,b,c = int(n[0]),int(n[4]),int(n[8])

if a + b == c:
    print("YES")
else:
    print("NO")