"""
Trên trục Ox tính từ vị trí 0, người ta muốn xếp nhiều nhất các đoạn thẳng sao cho không đoạn nào chồng lấn lên nhau. Đoạn thẳng thứ i có vị trí bắt đầu là X1[i] và kết thúc tại X2[i], với X1[i] <= X2[i].
Hãy tính số đoạn thẳng nhiều nhất có thể được lựa chọn để đưa lên trục Ox và không có đoạn nào chồng lấn lên nhau.

Input
Dòng đầu tiên ghi số bộ test, không quá 10.
Với mỗi bộ test: dòng đầu ghi số N là số đoạn thẳng (không quá 105)
Tiếp theo là N dòng, mỗi dòng có 2 số nguyên mô tả đoạn thẳng. Các giá trị tọa độ đều là các số nguyên không âm và không quá 106.

Output
Với mỗi test, viết trên 1 dòng số lượng đoạn thẳng nhiều nhất có thể được lựa chọn thỏa mãn điều kiện đề bài.

1
10
39 55
37 74
0 1
19 25
65 76
51 52
19 21
5 94
46 65
32 40
"""
def max_doan(doan):
    cnt = 0
    doan.sort(key = lambda x:x[1])
    end = -1
    for x1,x2 in doan:
        if x1 >= end:
            cnt += 1
            end = x2
    return cnt
t = int(input())

for _ in range(t):
    n = int(input())
    doan = [tuple(map(int,input().split())) for _ in range(n)]

    print(max_doan(doan))