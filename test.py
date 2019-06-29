#!/usr/bin/env python3

'''
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
'''


def solve(input_data):
    result = None
    # Viết code vào đây set result làm kết quả của tính toán
    r = [1] * (input_data + 1)
    M = []
    # tạo ma trận M 11x11
    for i in range(input_data + 1):
        M.append(r)
    # tinh cac phan tu trong ma tran
    for i in range(1, input_data + 1):
        for j in range(1, input_data + 1):
            M[i][j] = M[i - 1][j] + M[i][j - 1]

    result = M[input_data][input_data]
    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
