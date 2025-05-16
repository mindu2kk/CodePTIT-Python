"""
Một xâu ký tự là xâu palindrome là một xâu khác rỗng mà nếu lật ngược xâu ấy ta thu được xâu ban đầu.
Ví dụ các xâu abcba, dd là xâu palindrome, trong khi các xâu abc, ptit thì không phải.
Cho một xâu ký tự A. Tìm cách xoá đi nhiều nhất các kí tự của A để thu được một xâu palindrome.

Input
Một dòng duy nhất gồm một xâu kí tự S không quá 10000 ký tự, chỉ có các chữ cái in thường.

Output: Số kí tự lớn nhất có thể bỏ đi được để S là xâu palindrome.
"""

s = input()
print(len(s) - 1)