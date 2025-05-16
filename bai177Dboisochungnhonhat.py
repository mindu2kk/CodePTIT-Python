import sys

MOD = 10**9 + 7
MAXB = 10**6 + 5

is_prime = [True] * MAXB
is_prime[0] = is_prime[1] = False
primes = []
for p in range(2, MAXB):
    if is_prime[p]:
        primes.append(p)

        if p * p < MAXB:
            for i in range(p * p, MAXB, p):
                is_prime[i] = False

def legendre_exponent(n, p):
    exponent = 0
    power_of_p = p
    while power_of_p <= n:
        exponent += n // power_of_p
        if power_of_p > n // p:
            break
        power_of_p *= p
    return exponent

# Main logic for each test case
def solve():
    a, b = map(int, sys.stdin.readline().split())

    result = 1

    for p in primes:
        if p > b:
            break


        exponent_p_in_b_factorial = legendre_exponent(b, p)
        exponent_p_in_a_minus_1_factorial = legendre_exponent(a - 1, p)

        exponent = exponent_p_in_b_factorial - exponent_p_in_a_minus_1_factorial

        if exponent > 0:
            result = (result * (2 * exponent + 1)) % MOD

    print(result)


T = int(sys.stdin.readline())
for _ in range(T):
    solve()