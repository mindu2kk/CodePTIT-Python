"""
Cho hai dãy số A[] và B[] có cùng N phần tử. Dãy số A[] được gọi là phù hợp với dãy số B[]
khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A[] và B[] sao cho phần tử thứ i của A[] nhỏ hơn hoặc bằng phần tử thứ i của mảng B[]
(với tất cả vị trí trong dãy).
Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?

Input:
Dòng đầu tiên đưa vào số lượng bộ test T (T≤100).
Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 3 phần: phần thứ nhất là số N; phần thứ hai là N số của A[]; phần thứ 3 là N số của B[].
(1≤N≤100, 0≤A[i], B[i]≤1000)

Output:
Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A[] phù hợp với B[], ngược lại đưa ra “NO”.

2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
"""
def check(a,b,n):
    a.sort()
    b.sort()

    for i in range(n):
        if a[i] > b[i]:
            return "NO"
    return "YES"
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(check(a,b,n))