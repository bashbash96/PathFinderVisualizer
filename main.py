import pygame
from pygame.locals import QUIT, KEYDOWN, K_c, K_1, K_2, K_3

from Utils import manhattan_distance, euclidean_distance
from Grid import Grid
from WindowUtils import draw, get_cell_from_mouse_click, get_valid_number, show_message
from Strategy import Context
from SearchAlgorithms import BFS, AStar


def get_inputs():
    WIDTH = get_valid_number(message="The window width?\n(Recommended 800)", error_message="Enter a valid width!")
    ROWS = get_valid_number(message="The grid rows?\n(Recommended 20)", error_message="Enter a valid rows!")
    FPS = get_valid_number(message="Algorithm speed in milliseconds?\n(Recommended 50)",
                           error_message="Enter a valid speed time!")

    return WIDTH, ROWS, FPS


def left_mouse_pressed(curr_cell, start_position, end_position):
    if not start_position and curr_cell != end_position:
        curr_cell.make_start()
        start_position = curr_cell
    elif not end_position and curr_cell != start_position:
        curr_cell.make_end()
        end_position = curr_cell
    elif curr_cell != start_position and curr_cell != end_position:
        curr_cell.make_barrier()

    return start_position, end_position


def choose_algorithm(event, finder_context):
    if event.key == K_1:
        finder_context.set_strategy(BFS())
    elif event.key == K_2:
        finder_context.set_strategy(AStar(manhattan_distance))
    elif event.key == K_3:
        finder_context.set_strategy(AStar(euclidean_distance))


def start():
    pygame.init()
    WIDTH, ROWS, FPS = get_inputs()

    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("~ Path Finder Visualizer ~")
    grid = Grid(WIDTH, ROWS)

    start_position = None
    end_position = None
    finder_context = Context(BFS())

    run = True
    while run:
        draw(WIN, grid)
        event_list = pygame.event.get()

        for event in event_list:

            if event.type == QUIT:
                pygame.quit()
                run = False
                break

            if pygame.mouse.get_pressed(num_buttons=3)[0]:  # LEFT mouse button
                curr_cell = get_cell_from_mouse_click(grid)
                start_position, end_position = left_mouse_pressed(curr_cell, start_position, end_position)

            elif pygame.mouse.get_pressed()[2]:  # RIGHT mouse button
                curr_cell = get_cell_from_mouse_click(grid)
                curr_cell.reset()
                if curr_cell == start_position:
                    start_position = None
                elif curr_cell == end_position:
                    end_position = None

            if event.type == KEYDOWN:
                if not start_position or not end_position:
                    show_message('Invalid input!', 'You have to set the start and end points to run the algorithm')
                    continue
                valid_keys = [K_1, K_2, K_3, K_c]
                if event.key not in valid_keys:
                    continue

                if event.key == K_c:
                    start_position = None
                    end_position = None
                    grid = Grid(WIDTH, ROWS)
                    continue

                choose_algorithm(event, finder_context)

                found_path = finder_context.find(WIN, lambda: pygame.time.wait(FPS), grid, start_position, end_position)

                if not found_path:
                    show_message("Ops!", "No path found!")


start()
