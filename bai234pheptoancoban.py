"""
Cho một biểu thức trong phạm vi hai chữ số với các phép toán cộng trừ nhân chia. Các toán hạng và kết quả đảm bảo là số nguyên dương có hai chữ số, nếu có phép chia thì phải thỏa mãn tính chia hết.
Người ta có thể ẩn đi một số chữ số hoặc phép toán bằng cách điền dấu chấm hỏi (?). Nhiệm vụ của bạn là khôi phục các dấu chấm hỏi và in ra phép toán chính xác ban đầu. Nếu không thể có kết quả đúng thì ghi ra WRONG PROBLEM!

Dữ liệu vào
Dòng đầu ghi số bộ test T (1 ≤ T ≤ 100).
T dòng tiếp theo, mỗi dòng là một biểu thức có thể có các dấu ?.
Dữ liệu vào đảm bảo chỉ có duy nhất một kết quả đúng hoặc không thể có kết quả đúng.

Kết quả
Với mỗi bộ test, ghi ra biểu thức đúng tìm được. Hoặc WRONG PROBLEM

2
?0 ? 12 = 28
40 / ?3 = ??
"""

import itertools

# Các phép toán hợp lệ
operators = ['+', '-', '*', '/']

def evaluate_expression(a, op, b, c):
    """ Kiểm tra biểu thức có đúng không """
    if op == '+':
        return a + b == c
    elif op == '-':
        return a - b == c
    elif op == '*':
        return a * b == c
    elif op == '/':
        return b != 0 and a % b == 0 and a // b == c
    return False

def restore_expression(expression):
    """ Khôi phục biểu thức có chứa dấu '?' """
    parts = expression.split()
    possible_expressions = []

    # Duyệt qua mọi giá trị của A, B, C từ 10 đến 99
    for a, b, c in itertools.product(range(10, 100), repeat=3):
        for op in operators:
            # Tạo biểu thức thay thế `?`
            candidate = f"{a} {op} {b} = {c}"

            # Kiểm tra xem `candidate` có khớp với `expression`
            if len(expression) == len(candidate):
                match = True
                for i in range(len(expression)):
                    if expression[i] != '?' and expression[i] != candidate[i]:
                        match = False
                        break
                if match and evaluate_expression(a, op, b, c):
                    possible_expressions.append(candidate)

    # Nếu có đúng một biểu thức hợp lệ, trả về kết quả
    if len(possible_expressions) == 1:
        return possible_expressions[0]
    else:
        return "WRONG PROBLEM!"

# Đọc số bộ test
T = int(input().strip())

# Xử lý từng bộ test
for _ in range(T):
    expr = input().strip()
    print(restore_expression(expr))
