"""
Cho mảng A[] gồm N số nguyên khác nhau. Nhiệm vụ của bạn là đếm số lượng các bộ ba phần tử khác nhau có tổng là 0. Ví dụ A[] = {0, -1, 2, -3, 1}, ta nhận được kết quả là 2 vì có hai bộ 3: (0, -1, 1) và (2, -3, 1).

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
T, N, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤ N≤103; -109≤ A[i] ≤109;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
Ví dụ:

2
5
0 -1 2 -3 1
5
1 -2  1  0  5
"""

def sumTripleZero(a, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(sumTripleZero(a, n))
    t -= 1
    # Test case 2
    # 5
    # 0 -1 2 -3 1
    # 5
    # 1 -2  1  0  5

