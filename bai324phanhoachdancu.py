"""
Thành phố X mới xây dựng xong 2 khu đô thị mới và bắt đầu kế hoạch di chuyển dân cư. Có tổng cộng N người đăng kí chuyển đến khu đô thị mới, trong khi sức chứa của khu đô thị 1 và 2 chỉ là lần lượt C và D.
Chỉ số A[i] thể hiện mức độ giàu có của người thứ i. Ban quản lý dự án muốn sự giàu có ở 2 khu đô thị này là lớn nhất có thể. Chỉ số đánh giá được tính bằng tổng trung bình chỉ số giàu có của cư dân ở 2 khu độ thị mới (trung bình của khu đô thị 1 + trung bình khu đô thị 2).
Các bạn hãy tính xem khi sắp xếp tối ưu, chỉ số đánh giá này có giá trị lớn nhất bằng bao nhiêu?

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test bắt đầu bằng số nguyên N, C và D (1 ≤ N, C, D ≤ 100 000, C + D ≤ N).
Dòng tiếp theo gồm N số nguyên A[i] (1≤ A[i] ≤ 100 000).

Output:
Với mỗi test in ra đáp án trên một dòng, độ chính xác là 6 chữ số sau dấu phảy.

2
2 1 1
1 5
4 2 1
1 4 2 3
"""

t = int(input())

for _ in range(t):
    n,c,d = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse = True)
    minn = min(c,d)
    maxx = max(c,d)
    con = minn + maxx
    tong = sum(A[:minn])/minn + sum(A[minn:con])/maxx
    print(f'{tong:.6f}')