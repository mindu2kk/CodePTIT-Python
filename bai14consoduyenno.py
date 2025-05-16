"""
Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?

Input
Gồm nhiều dòng, mỗi dòng chứa một số nguyên dương n ghi ở hệ thập phân.
Giới hạn:
1≤n≤10^100

Output
Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số ntương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.
"""

t = int(input())

for _ in range(t):
    n = input()
    print("YES" if n[0] == n[-1] else "NO")
