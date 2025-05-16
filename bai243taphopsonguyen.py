"""
Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].

Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.

Input
Dòng đầu ghi 2 số n và m (1 < n,m <100).
Dòng thứ 2 ghi n số của a[].
Dòng thứ 3 ghi m số của b[].
Các số đều dương và nhỏ hơn 1000.

Output
Dòng đầu ghi tập giao của A và B
Dòng thứ 2 ghi tập A – B
Dòng thứ 3 ghi tập B - A

5 6
1 2 3 4 5
3 4 5 6 7 8
"""

n,m = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

giao = sorted(A & B)
hieuAB = sorted(A - B)
hieuBA = sorted(B - A)

print(*giao)
print(*hieuAB)
print(*hieuBA)