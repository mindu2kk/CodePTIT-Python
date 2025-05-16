"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.
Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.
Hãy liệt kê các số khác nhau xuất hiện trong A[] theo thứ tự tăng dần.

Input
Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

Output
Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A[] theo thứ tự tăng dần, mỗi số viết cách nhau một khoảng trống

124356141111434356149
"""

n = input()
A = set()
for i in range(0,len(n) - 1,2):
    A.add(int(n[i:i + 2]))

print(*sorted(A))