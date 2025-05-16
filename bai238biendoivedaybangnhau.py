def min_steps_to_equal_array(N, A):
    unique = []
    seen = set()

    for num in A:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    min_val = float('inf')
    best_value = None
    for num in unique:
        diff = sum(abs(d - num) for d in A)

        if diff < min_val:
            min_val = diff
            best_value = num
    print(min_val,best_value)

N = int(input().strip())
A = list(map(int, input().split()))

min_steps_to_equal_array(N, A)


"""
8
13 5 8 7 9 15 26 34
"""
