from math import sqrt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = pow(x1 - x2, 2)
    dy = pow(y1 - y2, 2)

    return sqrt(dx + dy)


def is_valid_num(num):
    return num.isdigit()


def is_valid_coordinates(rows, cols, row, col):
    return 0 <= row < rows and 0 <= col < cols
