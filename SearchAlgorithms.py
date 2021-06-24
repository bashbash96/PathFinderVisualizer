import pygame
from pygame.locals import QUIT
from queue import PriorityQueue

from collections import deque, defaultdict
from WindowUtils import update_cells
from Strategy import PathFinderStrategy


def generate_path(WIN, wait, parent, end):
    curr = end

    while curr:
        curr.make_path()
        update_cells(WIN, wait, [curr])
        curr = parent[curr]


class BFS(PathFinderStrategy):
    def find(self, window, wait, grid, start, end):
        parent = defaultdict()
        parent[start] = None
        queue = deque()
        queue.append(start)

        while queue:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return False

            curr_cell = queue.popleft()

            if curr_cell == end:
                generate_path(window, wait, parent, end)
                return True

            grid.update_neighbors(curr_cell)
            neighbors = curr_cell.get_neighbors()
            for neighbor_cell in neighbors:
                if neighbor_cell in parent:  # Already visited
                    continue

                parent[neighbor_cell] = curr_cell
                queue.append(neighbor_cell)
                if neighbor_cell != start and neighbor_cell != end:
                    neighbor_cell.make_open()

            if curr_cell != start and curr_cell != end:
                curr_cell.make_closed()
            update_cells(window, wait, [curr_cell] + neighbors)

        return False


class AStar(PathFinderStrategy):
    def __init__(self, distance_function):
        self.distance_function = distance_function

    def find(self, window, wait, grid, start, end):
        min_heap = PriorityQueue()
        min_heap.put((0, start))  # (heuristic distance, degree, cell)

        parent = defaultdict()
        parent[start] = None

        # g_score is the distance from the start cell to the current cell
        g_score = {cell: float('inf') for row in grid.cells for cell in row}
        g_score[start] = 0
        # h_score is the heuristic distance from the current cell to the end cell
        # f_score is the sum of g_score and h_score
        f_score = {cell: float('inf') for row in grid.cells for cell in row}
        f_score[start] = self.distance_function(start.get_position(), end.get_position())

        visiting = {start}

        while not min_heap.empty():
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return False

            curr_f_score, curr_cell = min_heap.get()
            visiting.discard(curr_cell)

            if curr_cell == end:
                generate_path(window, wait, parent, end)
                return True

            grid.update_neighbors(curr_cell)
            neighbors = curr_cell.get_neighbors()

            for neighbor_cell in neighbors:

                curr_g_score = g_score[curr_cell] + self.distance_function(curr_cell.get_position(),
                                                                           neighbor_cell.get_position())

                if curr_g_score < g_score[neighbor_cell]:
                    g_score[neighbor_cell] = curr_g_score
                    parent[neighbor_cell] = curr_cell

                    # calculate h-distance based on the distance function supplied by the user
                    h_score = self.distance_function(neighbor_cell.get_position(), end.get_position())
                    f_score[neighbor_cell] = curr_g_score + h_score

                    if neighbor_cell not in visiting:
                        # min_heap.put((h_score, neighbor_cell))
                        min_heap.put((f_score[neighbor_cell], neighbor_cell))
                        visiting.add(neighbor_cell)
                        if neighbor_cell != start and neighbor_cell != end:
                            neighbor_cell.make_open()

            if curr_cell != start and curr_cell != end:
                curr_cell.make_closed()
            update_cells(window, wait, [curr_cell] + neighbors)

        return False
