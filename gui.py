from tkinter import Canvas, Frame, BOTH

from enums import CellState


class MazeUI (Frame):
    def __init__ (self, parent):
        self.parent = parent
        self.parent.title ("MAZE")
        self.canvas = Canvas (height=600, width=600, bg='white')
        self.canvas.pack (fill=BOTH, expand=True)
        # self._create_grid()

    def paint_maze (self, matrix):
        rows = len (matrix)
        cols = len (matrix[0])
        _cell_color = ''
        for i in range (0, rows, 1):
            for j in range (0, cols, 1):
                if (matrix[i][j] == CellState.START.value):
                    _cell_color = 'red'
                elif (matrix[i][j] == CellState.BLOCKED.value):
                    _cell_color = 'black'
                elif (matrix[i][j] == CellState.UNBLOCKED.value):
                    _cell_color = 'white'
                elif (matrix[i][j] == CellState.VISITED.value):
                    _cell_color = 'pink'
                elif (matrix[i][j] == CellState.GOAL.value):
                    _cell_color = 'orange'

                self._paint_cell (i, j, _cell_color, rows)

    def _paint_cell (self, rw, cl, color, SIZE):
        delta = 20
        x0 = cl * delta
        x1 = x0 + delta
        y0 = rw * delta
        y1 = y0 + delta
        self.canvas.create_rectangle (
            x0, y0, x1, y1,
            fill=color, tags="cursor"
        )

    def _create_grid (self, event=None):
        w = self.canvas.winfo_width ()  # Get current width of canvas
        h = self.canvas.winfo_height ()  # Get current height of canvas

        # Creates all vertical lines at intevals of 100
        for i in range (0, w, 50):
            self.canvas.create_line (i, 0, i, h, tag='grid_line', fill='black')

        # Creates all horizontal lines at intevals of 100
        for i in range (0, h, 50):
            self.canvas.create_line (0, i, w, i, tag='grid_line', fill='black')
