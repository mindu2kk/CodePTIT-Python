"""

"""
from itertools import product


def generate_numbers(N):
    valid_digits = ['2', '3', '5', '7']
    results = []

    for length in range(4, N + 1):
        for num in product(valid_digits, repeat=length):
            num_str = ''.join(num)

            if num_str[-1] in "357" and all(d in num_str for d in "2357"):
                results.append(num_str)
    for number in sorted(results, key=int):
        print(number)

N = int(input().strip())
generate_numbers(N)

