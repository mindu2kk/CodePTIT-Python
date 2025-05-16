"""
Một dãy số A[] có n phần tử được coi là đẹp nếu thỏa mãn điều kiện sau:
max(A[i], A[i + 1]) ≤ 2 * min(A[i], A[i + 1])   (1 ≤ i ≤ n-1)
Ví dụ các dãy {1, 2, 3, 4}, {2, 4} được coi là các dãy số đẹp, còn các dãy số {5, 2}, {2,5}, {100, 1, 2} thì không phải.
Cho dãy số A[] có thể chưa thỏa mãn điều kiện “dãy số đẹp”.
Hãy cho biết cần chèn ít nhất bao nhiêu số (chèn vào bất kỳ chỗ nào trong mảng) để dãy số ban đầu trở thành dãy số đẹp.

Input

Dòng đầu tiên chứa một số nguyên t ( 1 ≤ t ≤ 1000) là số test.
Với mỗi test:
Dòng đầu ghi số nguyên n (2 ≤ n ≤ 50).
Dòng tiếp theo chứa n số nguyên a1, a2, …, an (1 ≤ ai ≤ 50)


Output

Với mỗi test in ra kết quả trên một dòng.

6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
"""
def dayso(n,a):
    cnt = 0
    for i in range(len(a) - 1):
        x,y = min(a[i],a[i + 1]),max(a[i],a[i + 1])
        while x * 2 < y:
            x *= 2
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(dayso(n,a))
