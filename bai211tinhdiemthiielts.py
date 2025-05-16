
"""
Điểm tổng của 4 kỹ năng sẽ được làm tròn số theo quy ước chung như sau:
Nếu điểm trung bình cộng của 4 kỹ năng có số lẻ là .25, thì sẽ được làm tròn lên thành .5, còn nếu là .75 sẽ được làm tròn thành 1.0.
Một trung tâm tổ chức thi thử Tiếng Anh cho các học viên.
Hãy giúp trung tâm tính điểm overall dựa trên kết quả bài làm của thí sinh nhé.

Input:
Dòng đầu cho số T là số lượng thí sinh
T dòng tiếp theo mỗi dòng cho 4 số là số câu đúng lần lượt của kỹ năng Reading, Listening, điểm kỹ năng speaking, và điểm kỹ năng writing.

Output:
In ra kết quả theo từng dòng.

2
15 25 5.0 5.5
22 32 6.0 6.0

"""
def get_band(x):
    bands = [(39, 40, 9.0), (37, 38, 8.5), (35, 36, 8.0), (33, 34, 7.5),
             (30, 32, 7.0), (27, 29, 6.5), (23, 26, 6.0), (20, 22, 5.5),
             (16, 19, 5.0), (13, 15, 4.5), (10, 12, 4.0), (7, 9, 3.5),
             (5, 6, 3.0), (3, 4, 2.5)]
    for a, b, band in bands:
        if a <= x <= b: return band
    return 0

def lamtron(x):
    nguyen = int(x)
    du = x - nguyen
    if du < 0.25:
        x = nguyen
    if du == 0.25:
        x = x - du + 0.5
    if du == 0.75:
        x = x - du + 1.0
    return float(x)

t = int(input())

for _ in range(t):
    l,r,s,w = map(float,input().split())

    point = (get_band(l) + get_band(r) + s + w) / 4
    print(lamtron(point))

