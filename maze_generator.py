import random

from enums import CellState


class MazeGenerator:
    def __init__ (self):
        pass

    """
    1 -> blocked
    0 -> not blocked
    2 -> start
    3 -> goal
    """

    def getNewMaze (self, ROWLEN, COLLEN, cell_blocked_probalility):
        grid = []
        self.MAXNUM = cell_blocked_probalility * 100
        self.MAXROW = ROWLEN
        self.MAXCOL = COLLEN

        for row in range (0, self.MAXROW, 1):
            rw = []
            for col in range (0, self.MAXCOL, 1):
                rand = random.randint (1, 100)
                if (rand < self.MAXNUM):
                    rw.append (CellState.BLOCKED.value)
                else:
                    rw.append (CellState.UNBLOCKED.value)
            grid.append (rw)

        grid[0][0] = CellState.START.value
        grid[self.MAXROW - 1][self.MAXCOL - 1] = CellState.GOAL.value

        return grid
