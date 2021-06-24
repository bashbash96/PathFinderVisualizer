from Cell import Cell
from Utils import is_valid_coordinates


class Grid:
    def __init__(self, width, rows):
        self.width = width
        self.rows = rows
        self.cols = rows
        self.cells = []
        self.__create_grid()

    def __create_grid(self):
        gap = self.width // self.rows

        for i in range(self.rows):
            self.cells.append([])
            for j in range(self.rows):
                new_cell = Cell(i, j, gap, self.rows)
                self.cells[-1].append(new_cell)

    def get_clicked_position(self, mouse_position):
        gap = self.width // self.rows
        y, x = mouse_position

        row = y // gap
        col = x // gap

        return row, col

    def get_cell(self, row, col):
        if not is_valid_coordinates(self.rows, self.cols, row, col):
            return None

        return self.cells[row][col]

    def update_neighbors(self, cell):
        if cell.neighbors:
            return

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        curr_row, curr_col = cell.row, cell.col
        for dx, dy in directions:
            neighbor_row, neighbor_col = curr_row + dx, curr_col + dy
            if not is_valid_coordinates(self.rows, self.cols, neighbor_row, neighbor_col):
                continue

            neighbor_cell = self.cells[neighbor_row][neighbor_col]
            if neighbor_cell.is_barrier():
                continue

            cell.add_neighbor(neighbor_cell)
