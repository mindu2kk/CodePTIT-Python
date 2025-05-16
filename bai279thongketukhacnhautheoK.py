"""
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""
import re
import string
from collections import Counter

n,k = map(int,input().split())
word =[]
dau = f"[{re.escape(string.punctuation)}]"

for _ in range(n):
    line = input().strip().lower()
    line = re.sub(dau,' ',line)
    word.extend(line.split())

dem = Counter(word)

sapxep = sorted(dem.items(),key = lambda x :(-x[1],x[0]))

for w,count in sapxep:
    if count >= k:
        print(w,count)