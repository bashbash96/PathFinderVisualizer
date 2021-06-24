import pygame
from Utils import GREY, WHITE, is_valid_num
from tkinter import messagebox
import tkinter as tk


def draw_grid_lines(win, grid):
    rows = grid.rows
    width = grid.width

    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid):
    win.fill(WHITE)

    for row in grid.cells:
        for cell in row:
            cell.draw_cell(win)

    draw_grid_lines(win, grid)
    pygame.display.update()


def update_cells(win, wait, cells):
    for cell in cells:
        if cell:
            cell.draw_cell(win)
        wait()

    pygame.display.update()


def get_cell_from_mouse_click(grid):
    mouse_position = pygame.mouse.get_pos()
    row, col = grid.get_clicked_position(mouse_position)
    return grid.get_cell(row, col)


def get_input(message):
    root = tk.Tk()
    root.focus()
    canvas1 = tk.Canvas(root, width=300, height=200, relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text=message)
    label1.config(font=('helvetica', 14))
    canvas1.create_window(150, 25, window=label1)

    entry1 = tk.Entry(root)
    canvas1.create_window(140, 80, window=entry1)
    entry1.focus()
    num = ''

    def result(event=None):
        nonlocal num
        num = entry1.get()
        nonlocal root
        root.quit()
        root.destroy()

    root.bind('<Return>', result)
    button1 = tk.Button(root, text='Submit', command=result, bg='brown', fg='white',
                        font=('helvetica', 12, 'bold'))

    canvas1.create_window(140, 120, window=button1)
    canvas1.focus_force()
    root.mainloop()
    return num


def show_message(title, message):
    tk.Tk().wm_withdraw()  # to hide the main window
    messagebox.showinfo(title, message)


def get_valid_number(message, error_message):
    while True:
        num = get_input(message)
        if not is_valid_num(num):
            show_message(error_message)
        else:
            return int(num)
