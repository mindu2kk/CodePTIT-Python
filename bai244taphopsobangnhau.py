"""
Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].
Tập A và tập B được coi là bằng nhau nếu số phần tử bằng nhau và tất cả các giá trị số từ nhỏ đến lớn đều bằng nhau từng đôi một. Khi A = B ta cũng có thể kết luận là hai dãy a[] và b[] chứa các số giống nhau.
Hãy kiểm tra xem A có bằng B hay không?

Input
Dòng đầu ghi 2 số n và m (1 < n,m <100).
Dòng thứ 2 ghi n số của a[].
Dòng thứ 3 ghi m số của b[].
Các số đều dương và nhỏ hơn 1000.

12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
"""
n,m = map(int,input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

if A == B:
    print("YES")
else:
    print("NO")