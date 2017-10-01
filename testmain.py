from Tkinter import Tk

from gui import MazeUI
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
from search_algorithms import SearchAlgorithms
import time
from simulate_annealiong import simulateAnnealing
from random import randint

### Generate 2dMaze where 3 is blocked and 2 is not blocked
def generate2DMaze(MAZESIZE, PROBABILITY):
	maze = []
	for i in range(0,MAZESIZE,1):
		inner = []
		for j in range(0,MAZESIZE,1):
			prob = randint(0,1)
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

## Print a clear version of maze
def printMaze(maze):
	for i in range(0, len(maze),1):
		for j in range(0,len(maze),1):
			print maze[i][j]
		print

def main ():
	PROBABILITY = 0.20
	MAZESIZE = 20
	maze = generate2DMaze(MAZESIZE,PROBABILITY)
	search = simulateAnnealing ()
	dim = MAZESIZE-1
	hardMaze = search.simulate_annealing_hard_maze(maze,0,0,dim,dim,PROBABILITY)
	printMaze(hardMaze)

if __name__ == '__main__':
	main ()
