"""
1.8. Напишите алгоритм, реализующий следующее условие: если элемент матрицы
MxN равен О, то весь столбец и вся строка обнуляются.
"""

Matrix = list[list]
Cell = tuple[int, int]


def check(matrix: Matrix) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                crossfill(matrix, (i, j), None)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] is None:
                matrix[i][j] = 0


def crossfill(matrix: Matrix, cell: Cell, value) -> None:
    for i in range(len(matrix)):
        matrix[i][cell[1]] = value
    for j in range(len(matrix[0])):
        matrix[cell[0]][j] = value


def main() -> None:
    matrix: Matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    check(matrix)
    print(*matrix, sep="\n")


if __name__ == "__main__":
    main()
