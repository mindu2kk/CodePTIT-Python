"""
Ngày thi chung kết ICPC PTIT 2020, các lập trình viên đang say sưa đọc đề và fix bug trong Hội trường 1, nhưng từ Ký túc xá thì nhóm bạn nữ xinh đẹp nào đó liên tục đồng thanh lặp đi lại lại câu hát quen thuộc:
“1, 2, 3, 5 anh có đánh rơi nhịp nào không?
Nếu câu trả lời là có …”
Để cho phù hợp với tình hình thời sự và giảm bớt căng thẳng cho các bạn thí sinh, ban tổ chức quyết định thêm một bài toán đơn giản: cho một dãy các số nguyên đếm tăng dần. Hỏi có số nào bị “đánh rơi” khi đếm hay không? Giả sử một dãy đếm chính xác thì luôn luôn đếm bắt đầu từ 1.

Dữ liệu vào:
Dòng đầu ghi số N là số con số được đếm (1 ≤ N ≤ 100)
Các dòng tiếp theo ghi đủ N số A[i] theo thứ tự tăng dần (1 ≤ A[i] ≤ 200). Các số phân cách bởi khoảng trống hoặc xuống dòng.

Kết quả:
Nếu phép đếm là đầy đủ, chính xác thì ghi ra Excellent!
Hoặc lần lượt liệt kê các số bị đánh rơi, mỗi số trên một dòng.

7
4 5 7 8 9
10 11
"""
N = int(input())
A = []

while len(A) < N:
    A.extend(map(int, input().split()))

missing = []
expected = 1

for num in A:
    while expected < num:
        missing.append(expected)
        expected += 1
    expected += 1
ok = 0
for d in missing:
    print(d)
    ok = 1
if ok == 0:
    print("Excellent!")