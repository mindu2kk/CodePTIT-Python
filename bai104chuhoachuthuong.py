def solve(s):
    lower_cnt = sum(1 for c in s if c.islower())
    upper_cnt = len(s) - lower_cnt

    if lower_cnt >= upper_cnt:
        print(s.lower())
    else:
        print(s.upper())

s = input().strip()
solve(s)