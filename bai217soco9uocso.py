"""
Cho số nguyên dương N. Hãy đếm các số nguyên dương không lớn hơn N và có đúng 9 ước số.

Input
Chỉ có một dòng ghi số N (1 ≤ N ≤ 109).

Output
Ghi ra số lượng các số có 9 ước số
"""
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_9_divisors(n):
    count = 0

    p = 2
    while p**8 <= n:
        if is_prime(p):
            count += 1
        p += 1

    primes = [i for i in range(2, int(math.sqrt(n)) + 1) if is_prime(i)]
    m = len(primes)
    for i in range(m):
        for j in range(i + 1, m):
            if primes[i]**2 * primes[j]**2 > n:
                break
            count += 1

    return count

n = int(input())
print(count_numbers_with_9_divisors(n))