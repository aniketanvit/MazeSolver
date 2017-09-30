from Tkinter import Tk

from gui import MazeUI
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
from search_algorithms import SearchAlgorithms
import time

def main ():
    PROBABILITY = 0.20
    MAZESIZE = 4500
    root = Tk ()
    grid = MazeUI (root)
    generator = MazeGenerator ()
    maze = generator.getNewMaze (MAZESIZE, MAZESIZE, PROBABILITY)
    solver = MazeSolver (SearchAlgorithms (maze))
    start_time = time.time()
    result = solver.solve_with_dfs (maze)
    print("Runtime: %s seconds" % ((time.time() - start_time)))
    #print (maze)
    #grid.paint_maze (maze)
    root.mainloop ()

if __name__ == '__main__':
    main ()
