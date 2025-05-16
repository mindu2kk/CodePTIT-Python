"""
Chung kết Euro 2020, quá nhiều người dự đoán đúng Italia thắng Anh bằng đá luân lưu 11m.
Ban tổ chức chương trình Dự đoán tỉ số trúng Mercedes thấy rất khó trao giải nên quyết định tìm người được trao thưởng bằng cách chạy đoạn code lựa chọn ngẫu nhiên.
Các người chơi dự đoán đúng được đánh số thứ tự bắt đầu từ 1, giả sử cũng có không quá 1000 người.
Chương trình sẽ thực hiện lấy ngẫu nhiên N lần, mỗi lần 1 giá trị từ 1 đến 1000, N cũng không quá 1000.
Sau khi kết thúc N lần ngẫu nhiên, con số nào được chọn nhiều lần nhất sẽ cho biết người trúng thưởng.
Trong trường hợp có nhiều số có số lần xuất hiện bằng nhau và lớn nhất thì số có giá trị nhỏ nhất sẽ được chọn.
Hãy giúp BTC tìm ra người được trao thưởng.

Input
Dòng đầu ghi số bộ test, không quá 100.
Mỗi bộ test gồm N+1 dòng. Dòng đầu ghi số N. Tiếp theo là N dòng ghi các giá trị ngẫu nhiên nhận được.

Output
Với mỗi test, ghi ra số thứ tự của người được trao thưởng.

3
3
999
999
19
4
13
333
333
13
3
11
12
13
"""

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    freq = {}
    for _ in range(n):
        num = int(input())
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_cnt = max(freq.values())
    winner = float('inf')

    for num,cnt in freq.items():
        if cnt == max_cnt and num < winner:
            winner = num
    res.append(winner)
    print("".join(map(str,res)))
    res.clear()
