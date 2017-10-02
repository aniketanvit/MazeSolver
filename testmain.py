############
## Author: Luisa McKenna
## copyright: McKenna <2017>
## 10/02/2017
## CS520 Assignment 1
############
from simulate_annealiong import simulateAnnealing
from Tkinter import Tk
from testGUI import MazeUI
from maze_generator import MazeGenerator
import random

### Generate 2dMaze where 3 is blocked and 2 is not blocked
def generate2DMaze(MAZESIZE, PROBABILITY):
	maze = []
	prob = PROBABILITY*100
	for i in range(0,MAZESIZE,1):
		inner = []
		for j in range(0,MAZESIZE,1):
			if (i == 0 and j == 0):
				inner.append("S")
			elif(i == MAZESIZE-1 and j == MAZESIZE-1):
				inner.append("G")
			else:
				rand = random.randint (1, 100)
				#print rand
				if(rand < prob):
					inner.append("F")
				else:
					inner.append("0")
		maze.append(inner)

	return maze

## Print a clear version of maze
def printMaze(maze):
	for row in maze:
		for j in row:
			print j,
		print

def main ():
	PROBABILITY = 0.20
	MAZESIZE = 10
	root = Tk ()
	grid = MazeUI (root)
	#for i in range(0,10,1):
	maze = generate2DMaze(MAZESIZE,PROBABILITY)
	search = simulateAnnealing ()
	dim = MAZESIZE-1
	hardMaze = search.simulate_annealing_hard_maze(maze,0,0,dim,dim,PROBABILITY)
	if(hardMaze != -1):
		#print "did we get here?"
		## used my own 2dMaze here and used gui.py to testGUI.py
		grid.paint_maze(hardMaze)
		print
	root.mainloop ()

if __name__ == '__main__':
	main ()
