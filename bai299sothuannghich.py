"""
Trong hệ cơ số thập phân, một số được gọi là thuận nghịch nếu đọc ngược lại ta vẫn thu được chính số đó. Ví dụ: 12321, 2345432, 111111 …
Chúng ta mở rộng khái niệm như sau: cho hệ cơ số K, giá trị thập phân x được gọi là thuận nghịch trong cơ số K nếu biểu diễn của x trong cơ số K có giá trị giống nhau khi viết xuôi và khi viết ngược. Với giả thiết biểu diễn trong hệ cơ số K bất kỳ (2 ≤ K ≤ 100000) là cách sử dụng chính các giá trị số từ 0 đến K-1 chứ không dùng các chữ cái.
Bài toán đặt ra là cho đoạn [a,b] và số M. Hãy đếm các số trong đoạn [a,b] là thuận nghịch trong tất cả các cơ số 2 ≤ K ≤ M.

Input:
Chỉ có một dòng ghi 3 số a,b,M.  0 ≤ a ≤ b ≤ 2 000 000; 2 ≤ M ≤ 100 000.

Output:
Ghi ra số lượng các số thỏa mãn.

1 356 2
18 118 13
"""

def is_palindrome(n, base):
    res = []
    while n > 0:
        res.append(n % base)
        n //= base
    return res == res[::-1]

def count_palindromes(a, b, m):
    count = 0
    for num in range(a, b + 1):
        if all(is_palindrome(num, base) for base in range(2, m + 1)):
            count += 1
    return count

def main():
    a, b, m = map(int, input().split())
    print(count_palindromes(a, b, m))

if __name__ == "__main__":
    main()
