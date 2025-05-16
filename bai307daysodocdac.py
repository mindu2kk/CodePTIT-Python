"""
Cho dãy số A[] có N phần tử. Một dãy con X chứa các phần tử liên tiếp của A[] được gọi là “độc nhất”, nếu như tồn tại một phần tử xuất hiện duy nhất đúng một lần trong X.
Dãy số A[] được gọi là “độc đắc” nếu như mọi dãy con liên tiếp có độ dài nhỏ hơn N đều là dãy số độc nhất. Nhiệm vụ của bạn là xác định xem dãy số đã cho có phải là “độc đắc” hay không?

Dữ liệu vào:
Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 20).
Mỗi test gồm số đầu tiên là số lượng phần tử N (2 ≤ N ≤ 105)
Dòng tiếp theo gồm N số nguyên không âm A[i], có giá trị không vượt quá 109.

Kết quả:
Với mỗi test, hãy in ra đáp án tìm được trên một dòng. Nếu dãy số là độc đắc, in ra “YES”. In ra “NO” trong trường hợp ngược lại.

5
5
1 2 3 4 5
7
1 2 3 4 3 4 1
5
1 1 1 1 1
5
1 2 5 2 1
5
5 5 2 5 5
"""

from collections import Counter


def is_doc_dac(arr, N):
    count = Counter(arr[:N - 1])  # Đếm số lần xuất hiện trong cửa sổ đầu tiên

    # Kiểm tra từng cửa sổ con
    for i in range(N - 1, len(arr)):
        count[arr[i]] += 1  # Thêm phần tử mới vào cửa sổ

        # Kiểm tra xem có số nào xuất hiện đúng một lần không
        if any(v == 1 for v in count.values()):
            # Di chuyển cửa sổ (xóa phần tử cũ đi)
            count[arr[i - (N - 1)]] -= 1
            if count[arr[i - (N - 1)]] == 0:
                del count[arr[i - (N - 1)]]
        else:
            print("NO")
            return

    print("YES")


# Đọc dữ liệu
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    is_doc_dac(arr, N)
