S1 = input()
S2 = input()
p = int(input())

result = S1[:p-1] + S2 + S1[p-1:]

print(result)
