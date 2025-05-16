"""
Sau khi xem Olympic Tokyo 2020, Nam nhận thấy ở một số nội dung thi có chấm điểm thì điểm được tính cho vận động viên sẽ
bỏ qua các giá trị điểm thấp nhất và cao nhất sau đó mới tính trung bình.
Nam mở rộng bài toán như sau: Có N giám khảo, mỗi giám khảo cho một giá trị điểm là một số thực trong đoạn từ 0 đến 10.
Hãy loại bỏ các giá trị điểm bằng với điểm thấp nhất hoặc cao nhất, sau đó in ra điểm trung bình của các giá trị còn lại.
Dữ liệu vào của bài toán đảm bảo luôn có ít nhất 3 giá trị khác nhau trong các giá trị điểm ban đầu.

Input
Dòng đầu ghi số N là số giám khảo (không quá 100).
Dòng thứ 2 ghi N giá trị điểm, là các số thực trong đoạn [0,10] - đảm bảo luôn có ít nhất 3 giá trị khác nhau.

Output
Ghi ra giá trị điểm trung bình sau khi đã loại bỏ các giá trị nhỏ nhất và lớn nhất. Kết quả được ghi với đúng 2 số phần thập phân.
6
6.75 8 9.2 7.25 7.75 6.75
"""
n = int(input())
A = list(map(float,input().split()))

min_val = min(A)
max_val = max(A)

filtered = [s for s in A if s != min_val and s != max_val]

avg_score = sum(filtered) / len(filtered)

print(f"{avg_score:.2f}")