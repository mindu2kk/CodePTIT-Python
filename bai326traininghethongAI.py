"""
Một hệ thống nhận diện khuôn mặt gồm có N module. Mỗi module có khả năng hoạt động chính xác bằng P[i].
Xác suất hoạt động chính xác của hệ thống được xác định bằng tích của tất cả các module.
Để tăng độ chính xác của hệ thống, bạn phải thực hiện train dữ liệu cho mỗi module.
Tuy nhiên, việc này mất rất nhiều thời gian và bạn chỉ có tổng cộng U đơn vị thời gian.
Train một model trong X đơn vị thời gian, độ chính xác của module này tăng lên thêm X (tối đa là bằng 1).
Bạn hãy xác định xem sau khi training, độ chính xác lớn nhất mà hệ thống đạt được là bao nhiêu?

Input:
Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 100).
Mỗi test gồm số nguyên dương N (1 ≤ N ≤ 50).
Dòng tiếp theo là số thực U.
Dòng cuối gồm N số thực P[i] (0 ≤ P[i] ≤ 1).

Output:
Với mỗi test in ra trên một dòng đáp án tìm được với độ chính xác 10^-6.

2
4
1.4000
0.5000 0.7000 0.8000 0.6000
2
1.0000
0.0000 0.0000
"""

def tryy(n,u,P):
    P.sort()
    for i in range(n):
        if i < n - 1:
            kc = (P[i + 1] - P[i]) * (i + 1)
            if u >= kc:
                u -= kc
                for j in range(i + 1):
                    P[j] = P[i + 1]
            else:
                tang = u / (i + 1)
                for j in range(i + 1):
                    P[j] += tang
                u = 0
                break
    if u > 0:
        tang = u / n
        for i in range(n):
            P[i] = min(1,P[i] + tang)
    res = 1.0
    for i in range(n):
        res *= P[i]

    print(f"{res:.6f}")

t = int(input())

for _ in range(t):
    n = int(input())
    u = float(input())
    P = list(map(float,input().split()))
    tryy(n,u,P)