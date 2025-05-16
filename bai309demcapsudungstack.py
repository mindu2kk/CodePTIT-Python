"""

7
2
4
1
2
2
5
1
"""
from collections import deque

sz = int(input())
stk = deque()
stk.append([int(input()), 1])
cnt = 0
for i in range(1,sz):
    cur = int(input())
    while len(stk) > 0:
        top = stk.pop()
        if top[0] > cur:
            cnt += 1
            stk.append(top)
            stk.append([cur, 1])
            break
        elif top[0] == cur:
            cnt += top[1]
            if len(stk) > 0:
                cnt += 1
            stk.append([cur, top[1] + 1])
            break
        else:
            cnt += top[1]
    if len(stk) == 0:
        stk.append([cur, 1])
print(cnt)
