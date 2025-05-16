"""
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). Ví dụ số 11 không phải là số Emirp Number. Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả.
"""
from math import isqrt

def nto(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())

for _ in range(t):
    n = input()
    A = []
    for i in range(13,int(n)):
        if nto(i) and nto(int(str(i)[::-1])) and str(i) != str(i)[::-1] and int(str(i)[::-1]) < int(n) and i not in A and int(str(i)[::-1]) not in A:
            A.append(i)
            A.append(str(i)[::-1])
    print(*A)
