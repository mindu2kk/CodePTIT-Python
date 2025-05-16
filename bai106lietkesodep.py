"""
Cho số nguyên dương N, hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:

Chỉ có các chữ số 0,2,4,6,8
Số chữ số của N chia cho 2 dư 1
Input

Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

Output

Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.
"""

# Ktra thuan nghich

# Kiểm tra số thuận nghịch
def is_palindrome(num_str):
    return num_str == num_str[::-1]

# Kiểm tra chỉ chứa các chữ số chẵn (0, 2, 4, 6, 8)
def has_even_digits_only(num_str):
    return all(c in '02468' for c in num_str)

# Xử lý từng test
def process_test_case(N):
    results = []
    for num in range(22, N):
        num_str = str(num)
        if len(num_str) % 2 == 0 and is_palindrome(num_str) and has_even_digits_only(num_str):
            results.append(num_str)
    return " ".join(results)

T = int(input())  # Nhập số lượng bộ test
for _ in range(T):
    N = int(input())
    print(process_test_case(N))  # Sửa lỗi bằng cách in trực tiếp


