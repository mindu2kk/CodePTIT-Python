"""
Xâu ký tự S được tạo ra bằng cách bổ sung dần các ký tự chữ cái Tiếng Anh in hoa như sau.
Bước 1: Chỉ có chữ cái A
Bước 2: Thêm chữ cái B vào giữa 2 chữ A => S = "ABA"
Bước 3: Thêm chữ cái C vào giữa 2 xâu đã có ở bước 2: S = "ABACABA"
Cứ như vậy cho đến bước thứ N (0 < N < 26)
Hãy xác định ký tự thứ K trong bước biến đổi thứ N là chữ cái gì?

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm số nguyên dương N và K (1 ≤ N ≤ 25, 1 ≤ K ≤ 2N - 1).

Output:
Với mỗi test, in ra đáp án trên một dòng.

2
3 2
4 8
"""
def findK(n,k):
    if k == 2 ** (n -1):
        return chr(ord('A') + n - 1)
    if k < 2 ** (n - 1):
        return findK(n-1,k)
    else:
        return findK(n - 1,k - 2 ** (n - 1))

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    print(findK(n,k))