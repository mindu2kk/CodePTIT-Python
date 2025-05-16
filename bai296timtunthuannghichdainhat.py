"""
Cho dữ liệu vào dạng file văn bản.
Hãy tìm ra từ thỏa mãn tính chất thuận nghịch và có độ dài lớn nhất trong file đó. Đếm xem từ đó xuất hiện bao nhiêu lần.
Nếu có nhiều từ cùng có độ dài lớn nhất thì in ra tất cả các từ đó theo thứ tự xuất hiện trong file ban đầu.

Input: File văn bản VANBAN.in Không quá 1000 từ.

Output:
Ghi ra trên màn hình một dòng từ thuận nghịch có độ dài lớn nhất và số lần xuất hiện của nó. Nếu có nhiều từ cùng có độ dài lớn nhất thì các từ được liệt kê theo thứ tự xuất hiện ban đầu.
"""
from collections import Counter


def is_palin(word):
    return word == word[::-1]

longest_palindrome = ''
max_length = 0
palindrome_count = 0

with open('VANBAN.in', 'r') as file:
    text = file.read()
    words = [word.lower() for line in text for word in line.split() if is_palin(word)]

    counter = Counter(words)
    max_length = max(len(word) for word in counter)

    for words in counter:
        if len(words) == max_length:
            print(words, counter[words])