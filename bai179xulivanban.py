import re
import sys

text = " ".join(sys.stdin.read().split())

sentences = re.split(r'[.!?]',text)

for sentence in sentences:
    words = sentences.splits()
    if words:
        print(words[0].capitalize(),*map(str.lower,words[1:]))

"""
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
"""