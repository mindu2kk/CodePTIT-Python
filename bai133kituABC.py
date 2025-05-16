"""
Hãy liệt kê tất cả các xâu ký tự có độ dài không quá N, chỉ tạo bởi các ký tự A, B, C và thỏa mãn các điều kiện sau:
Chứa cả ba ký tự A, B, C
Số ký tự A không nhiều hơn số ký tự B, số ký tự B không nhiều hơn số ký tự C

Input
Chỉ có một dòng ghi số N, không quá 12.

Output
Ghi ra lần lượt các xâu thỏa mãn theo thứ tự độ dài từ ngắn nhất đến dài nhất.
Nếu có cùng độ dài thì ghi theo thứ tự từ điển.
Mỗi xâu ghi trên một dòng.
"""
from itertools import product
from timeit import repeat


def valid(s):
    if not all(c in s for c in "ABC"):
        return False
    num_a = s.count('A')
    num_b = s.count('B')
    num_c = s.count('C')

    return num_a <= num_b <= num_c

def test(n):
    res = []
    for length in range(3,n + 1):
        for s in product('ABC',repeat = length):
            s = ''.join(s)
            if valid(s):
                print(s)

n = int(input())
test(n)
