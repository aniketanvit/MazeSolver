from Tkinter import Tk

from gui import MazeUI
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
from search_algorithms import SearchAlgorithms
import time
from depthFirstAlgo import depth_first_algo

### Generate 2dMaze where 3 is blocked and 2 is not blocked
def generate2DMaze(MAZESIZE, PROBABILITY):
	maze = []
	for i in range(0,MAZESIZE-1,1):
		inner = []
		for j in range(0,MAZESIZE-1,1):
			prob = random(0,1)
			if(prob< PROBABILITY):
				inner.append(3)
			else:
				inner.append(2)
		maze.append(inner)
	## Start
	maze[0][0] == 1
	## Goal
	maze[MAZESIZE-1][MAZESIZE-1] = 5
	return maze

def main ():
	PROBABILITY = 0.20
	MAZESIZE = 20
	maze = generate2DMaze(MAZESIZE,PROBABILITY)
	search = simulateAnnealing()
	hardMaze = search.searchHardestMaze(maze, 0,0, MAZESIZE-1,MAZESIZE-1, PROBABILITY)
	print hardMaze
