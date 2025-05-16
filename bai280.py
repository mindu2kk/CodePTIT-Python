import re
def ThongKe(s):
    ktdb = re.compile('\W')
    s = re.sub(ktdb, ' ', s.lower())
    words = re.findall(r'[a-zA-Z]+', s)

    dif_words = []
    for word in set(words):
        dif_words.append({'word': word, 'count' : words.count(word) })

    res = sorted(dif_words, key = lambda k:(-k['count'], k['word']))
    for dic in res:
        print(dic.get('word'), dic.get('count'))

t = int(input())
s = ""
while t>0:
    s += input() +" "
    t-=1
ThongKe (s)