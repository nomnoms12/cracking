"""
1.8. Напишите алгоритм, реализующий следующее условие: если элемент матрицы
MxN равен О, то весь столбец и вся строка обнуляются.
"""

Matrix = list[list]
Cell = tuple[int, int]


def main() -> None:
    matrix: Matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    check(matrix)
    print(*matrix, sep="\n")


def check(matrix: Matrix) -> None:
    zeros = find_zeros(matrix)
    for i, j in zeros:
        fill_row(matrix, i)
        fill_col(matrix, j)


def find_zeros(matrix: Matrix) -> list[Cell]:
    zeros = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    return zeros


def fill_row(matrix: Matrix, i: int) -> None:
    for j in range(len(matrix[0])):
        matrix[i][j] = 0


def fill_col(matrix: Matrix, j: int) -> None:
    for i in range(len(matrix)):
        matrix[i][j] = 0


if __name__ == "__main__":
    main()
