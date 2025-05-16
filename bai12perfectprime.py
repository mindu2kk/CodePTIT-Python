"""
Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤107;
Output:

Đưa ra kết quả mỗi test theo từng dòng.
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    for i in range(len(n)):
        if not is_prime(int(n[i])):
            return False
    return True
t = int(input())

for _ in range(t):
    n = input()
    if is_prime(int(n)) and is_prime(int(n[::-1])) and is_prime(sum(map(int, n))) and check(n):
        print("Yes")
    else:
        print("No")

