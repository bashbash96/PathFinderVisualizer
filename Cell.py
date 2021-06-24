import pygame

from Utils import WHITE, BLACK, GREEN, RED, \
    PURPLE, ORANGE, BLUE


class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.neighbors = []
        self.color = WHITE
        self.x = row * width
        self.y = col * width

    def get_position(self):
        return self.row, self.col

    def is_empty(self):
        return self.color == WHITE

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == BLUE

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def reset(self):
        self.color = WHITE

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_path(self):
        self.color = PURPLE

    def draw_cell(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def add_neighbor(self, cell):
        self.neighbors.append(cell)

    def get_neighbors(self):
        return self.neighbors

    def __lt__(self, other):
        return self.row < other.row or self.col < other.col
