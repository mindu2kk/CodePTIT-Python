"""Cho dãy số nguyên A[] gồm có N phần tử. Nhiệm vụ của bạn là tìm dãy số B[] có tổng phần tử nhỏ nhất thỏa mãn tính chất A[i] / B[i] = A[i+1] / B[i+1] với mọi chỉ số i (0 ≤ i ≤ N-2).

Phép chia trong bài toán này là phép chia nguyên (tức là chỉ lấy phần nguyên của kết quả: ví dụ 5/3 = 1).

Dữ liệu vào:

Dòng đầu tiên là số lượng phần tử N (1 ≤ N ≤ 1000).

Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 2000).

Kết quả:

In ra một số nguyên là tổng các phần tử của dãy số B[] tìm được.
"""

def check(p, a):
    for x in a:
        if int(x / p) == int(x / (p + 1)):
            return False
    return True
def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    end = min(a)
    res = 0
    for i in range(end, 0, -1):
        if (check(i, a)):
            for j in range(n):
                res += int(a[j] / (i + 1)) + 1
            break
    print(res)

if __name__ == '__main__':
    main()