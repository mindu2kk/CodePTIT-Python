"""
Trong thơ ca có rất nhiều các thể thơ và những cách gieo vần khác nhau cho các bài thơ. Trong số những thể thơ đó, bạn có thể lựa chọn cho mình một loại thể thơ riêng để đem lại nhiều hiệu quả cho bài thơ và giúp cho bạn có thể thấy được sự hiệu quả trong cách truyền đạt những cung bậc cảm xúc vào trong bài thơ.
Cho danh sách các bài thơ gồm hai thể loại thơ lục bát và thơ thất ngôn tứ tuyệt.
1. Thơ lục bát
- Số chữ và số câu: Một cặp hai câu thơ, câu trên sáu chữ (lục), câu dưới tám chữ (bát). Một bài thơ có thể có nhiều cặp lục bát, số lượng cặp câu không hạn định.
2. Thơ thất ngôn tứ tuyệt
- Là bài thơ mà mỗi dòng 7 tiếng, bài có 4 câu
Nhiệm vụ của bạn là hãy viết chương trình xác định số lượng bài thơ và thể thơ (ghi bằng số) của từng bài từ danh sách các bài thơ có sẵn.
Input:
Dòng đầu tiên cho số N là tổng số dòng của tất cả các bài thơ.
N dòng tiếp theo ghi lại các câu thơ của từng bài. Các bài thơ lục bát sẽ đảm bảo không đặt liên tiếp nhau.
Output:
In ra kết quả số bài thơ và số tương ứng với thể thơ theo từng dòng.

8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
"""

def cnt(sent):
    return len(sent.split())

def test(n,sent):
    poems = []
    i = 0

    while i < n:
        if i + 1 < n and cnt(sent[i]) == 6 and cnt(sent[i + 1]) == 8:
            poems.append(1)
            i += 2
            while i + 1 < n and cnt(sent[i]) == 6 and cnt(sent[i + 1]) == 8:
                i += 2
        elif i + 3 < n and all(cnt(sent[i + j]) == 7 for j in range(4)):
            poems.append(2)
            i += 4
        else:
            i += 1
    print(len(poems))
    for poem in poems:
        print(poem)


n = int(input())
sent = [input().strip() for _ in range(n)]

test(n,sent)