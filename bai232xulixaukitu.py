"""
Trong lập trình cơ bản, một từ được hiểu là một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.
Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng. Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. Các từ đều được chuyển hết về chữ viết thường.

Input
Chỉ có 2 dòng, mỗi dòng có độ dài không quá 1000 ký tự.

Output
Dòng 1 ghi hợp của 2 tập từ theo thứ tự từ điển
Dòng 2 ghi giao của 2 tập từ theo thứ tự từ điển.

Lap trinh huong doi tuong
Ngon ngu lap trinh C++
"""

s1 = input().lower().split()
s2 = input().lower().split()
set1 = set(s1)
set2 = set(s2)

giao = sorted(set1 & set2)
hop = sorted(set1 | set2)

print(*hop)
print(*giao)