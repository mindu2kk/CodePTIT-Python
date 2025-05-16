
"""
Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).
Hãy liệt kê các từ khác nhau xuất hiện trong đoạn văn bản theo thứ tự số lần xuất hiện giảm dần.
Chú ý:
Khi thống kê thì không phân biệt chữ hoa, chữ thường.
Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ

Input
Dòng đầu ghi số N không quá 1000.
Tiếp theo là N dòng mô tả văn bản. Mỗi dòng không quá 500 ký tự.

Output
Ghi ra danh sách các từ (ở dạng in thường) theo thứ tự số lần xuất hiện giảm dần.
Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.

3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT y z.
"""
import re
def ThongKe(s):
    ktdb = re.compile('\W')
    s = re.sub(ktdb, ' ', s.lower())
    words = s.split()

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
ThongKe(s)