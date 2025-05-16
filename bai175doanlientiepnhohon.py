"""
Cho dãy số A[] có N phần tử. Với mỗi vị trí thứ i trong dãy,
hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước mà các giá trị đều nhỏ hơn hoặc bằng A[i].

Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.
Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 105).
Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ A[i] ≤ 106).

Output
Với mỗi bộ test, in ra dãy kết quả trên một dòng.

1
7
100 80 60 70 60 75 85
"""

def check(A,n):
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        res[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    return res


# Đọc input và xử lý
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(*check(A,N))

