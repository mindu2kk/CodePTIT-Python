"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.
Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.
Nhập thêm số nguyên dương K gọi là giá trị ngưỡng tối thiểu. Hãy liệt kê các số xuất hiện từ K lần trở lên trong dãy A[] theo thứ tự từ nhỏ đến lớn.

Input
Dòng đầu ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.
Dòng thứ 2 ghi số nguyên dương K (không quá 100).

Output

Ghi ra lần lượt các số khác nhau của dãy A[] thỏa mãn xuất hiện ít nhất K lần và số lần xuất hiện tương ứng, mỗi số viết trên một dòng theo thứ tự tăng dần.
Nếu không có số nào thỏa mãn ghi ra dòng chữ NOT FOUND
"""
from collections import Counter

n = input()
k = int(input())
A = []
seen = set()
B = []
for i in range(0,len(n) -1,2):
    B.append(int(n[i:i + 2]))

for i in range(0,len(n) -1,2):
    if int(n[i:i + 2]) not in seen:
        A.append(int(n[i:i + 2]))
        seen.add(int(n[i:i + 2]))

count = Counter(B)
A = sorted(A)
ok = 0
for d in A:
    if count[d] >= k:
        print(d,count[d])
        ok = 1
if ok == 0:
    print("NOT FOUND")