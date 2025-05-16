"""
Cho hai số nguyên dương X1, X2. Ta chỉ được phép thay đổi chữ số p thành chữ số q và ngược lại chữ. Hãy đưa ra tổng nhỏ nhất và tổng lớn nhất các số X1 và X2 được tạo ra theo nguyên tắc kể trên.

Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm 3 dòng: dòng đầu tiên ghi lại chữ số p và chữ số q; hai dòng kế tiếp ghi lại các số X1 và X2 theo thứ tự.
T, X1, X2 thỏa mãn ràng buộc: 1≤ T ≤100; 0≤ X1, X2 ≤101000.

Output:
Đưa ra kết quả mỗi test theo từng dòng.

1
5 6
645
666
"""

n = int(input())

def chuyen(a,b,p,q):
    a = a.replace(p,q)
    b = b.replace(p,q)
    return int(a) + int(b)

while n > 0:
    [p,q] = input().split()
    s = input().split()
    if len(s) > 1:
        a,b = s[0],s[1]
    else:
        a = s[0]
        b = input()

    x = chuyen(a,b,p,q)
    y = chuyen(a,b,q,p)

    print(min(x,y),max(x,y))
    n -= 1