from tkinter import Tk

from gui import MazeUI
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
from search_algorithms import SearchAlgorithms


def main ():
    PROBABILITY = 0.23
    MAZESIZE = 20

    root = Tk ()
    grid = MazeUI (root)
    generator = MazeGenerator ()
    maze = generator.getNewMaze (MAZESIZE, MAZESIZE, PROBABILITY)
    solver = MazeSolver (SearchAlgorithms (maze))
    result = solver.solve_with_dfs (maze)
    print (maze)
    grid.paint_maze (maze)
    root.mainloop ()


if __name__ == '__main__':
    main ()
