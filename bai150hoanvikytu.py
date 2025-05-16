"""
Cho xâu ký tự S có không quá 9 ký tự chữ cái in hoa, không có khoảng trống. Các ký tự khác nhau từng đôi một và đã được sắp xếp từ trái sang phải theo thứ tự từ điển.
 Hãy liệt kê tất cả các hoán vị của xâu ký tự S theo đúng thứ tự từ điển, mỗi hoán vị trên một dòng.
Input
Chỉ có một dòng ghi xâu S, độ dài không quá 9

Output
Ghi lần lượt các hoán vị theo thứ tự từ điển, mỗi xâu trên một dòng.
Chú ý: hoán vị đầu tiên chính là xâu S.
"""
from itertools import permutations

s = input().strip()

for char in permutations(s):
    print(''.join(char))

