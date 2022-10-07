"""
1.8. Напишите алгоритм, реализующий следующее условие: если элемент матрицы
MxN равен О, то весь столбец и вся строка обнуляются.
"""

Matrix = list[list]


# def zeros(row: list) -> None:
#     for i in range(len(list)):
#         row[i] = 0


def check(matrix: Matrix, n: int, m: int) -> None:
    ...
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j] == 0:
    #             zeros(matrix[i])


def main():
    matrix: Matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    check(matrix, 3, 3)
    print(*matrix, sep="\n")


if __name__ == "__main__":
    main()
