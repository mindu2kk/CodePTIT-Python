"""
Cho một số nguyên dương N.
Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.
Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.

Input:
Dòng đầu ghi số bộ test (không quá 1000).
Mỗi test ghi số N (1 ≤ N ≤ 1018)

Output:
Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.
"""

def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        rn = int(str(n)[::-1])
        n += rn
    return -1


for t in range(int(input())):
    n = int(input())
    print(solve(n))