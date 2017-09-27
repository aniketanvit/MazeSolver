from enum import Enum


class MazeState (Enum):
    UNSOLVED = 1,
    SOLVED = 2,
    UNSOLVABLE = 3


class CellState (Enum):
    START = 1
    UNBLOCKED = 2
    BLOCKED = 3
    VISITED = 4
    GOAL = 5
