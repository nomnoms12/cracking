"""
1.7. Имеется изображение, представленное матрицей NxN; каждый пиксел пред
ставлен 4 байтами. Напишите метод для поворота изображения на 90 градусов.
Удастся ли вам выполнить эту операцию «На месте»?
"""

Image = list[list[str]]


def rotate_90(image: Image) -> None:
    n = len(image)

    for k in range(n // 2):
        e = n - k - 1
        for i in range(n - k * 2 - 1):
            image[k][k + i], image[k + i][e] = image[k + i][e], image[k][k + i]
            image[k][k + i], image[e][e - i] = image[e][e - i], image[k][k + i]
            image[k][k + i], image[e - i][k] = image[e - i][k], image[k][k + i]


def main() -> None:
    image: Image = [
        ["0", "1", "2", "3", "4"],
        ["5", "6", "7", "8", "9"],
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
    ]

    rotate_90(image)
    print(*image, sep="\n")


if __name__ == "__main__":
    main()
