############
## Author: Luisa McKenna
## copyright: McKenna <2017>
## 10/02/2017
## CS520 Assignment 1
############

import random
import math
x = [0,0,1,-1]
y = [1,-1,0,0]

accept_prob = 0
path = []
fringe_queue = []

# printMaze  prints a simplified version of the maze
#
# param maze
def printMaze(maze):
	for row in maze:
		for j in row:
			print j,
		print

# Generate2DMaze  generates a 2d list
#
# S - Start
# G - Goal
# F - Full
# 0 - Empty

# param  MAZESIZE, PROBABILITY
# return  maze
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
				if(rand < prob):
					inner.append("F")
				else:
					inner.append("0")
		maze.append(inner)

	return maze

# directions  finds all possible directions a cell has and adds to fringe
#
# param  maze, intial x, intial y, goal x, goal y, and fringe
#def directions(maze,cx,cy, gx,gy, fringe_queue, nodes):
def directions(maze,cx,cy, gx,gy, fringe_queue):
	for i in range(0,4,1):
		row = cx + x[i]
		col = cy + y[i]
		if(row >= 0 and row <= gx and col >= 0 and col <= gy and (maze[row][col] == "0" or maze[row][col] == "G")):
			if (cx == 0 and cy == 0):
				maze[row][col] = "1"
			else:
				maze[row][col] = str(1 + int(maze[cx][cy]))
			fringe_queue.append([row,col])
			#nodes += 1;

# Breadth  first search to find the most optimal path
#
# param  maze, intial x, intial y, goal x, goal y
# return  minmial path if exists or -1 if it doesn't
def search_algo_bfs(maze, sx,sy, gx,gy):
	#nodes_expanded = 0
	path[:] = []
	fringe_queue[:] = []
	fringe_queue.append([sx,sy])
	while fringe_queue:
		current_state = fringe_queue.pop(0)
		cx = current_state[0]
		cy = current_state[1]
		#node_expanded = directions(maze,cx,cy,gx,gy,fringe_queue,nodes_expanded)
		directions(maze,cx,cy,gx,gy,fringe_queue)
		if len(fringe_queue) != 0:
			peek = fringe_queue[0]
			peekx = peek[0]
			peeky = peek[1]
			if(peekx == gx and peeky == gy):
				#return 1 + int(maze[cx][cy])
				return nodes_expanded + 1
		path.append(current_state)
	return -1

# simulateAnnealing  defines the simulateAnnealing algorithm
# to find the hardest maze
class simulateAnnealing:

	# Simulate annealing  finds hardest path
	#
	# param  maze, intial x, intial y, goal x, goal y, probability cell is full
	# return  hard_maze if exists or -1 if it doesn't
	def simulate_annealing_hard_maze(self,maze,sx,sy,gx,gy,prob):
		current_Maze = maze
		current_performance = search_algo_bfs(maze, sx,sy, gx,gy)
		if current_performance == -1:
			return -1
		alpha = 0.9
		T_MAX = 40
		TIME = 1
		while(TIME < T_MAX):
			prob += 0.01
			new_maze = generate2DMaze(10, prob)
			new_performance = search_algo_bfs(new_maze, sx,sy, gx,gy)
			if(new_performance != -1):
				if(new_performance > current_performance):
					current_Maze = new_maze
					current_performance = new_performance
				else:
					randProb = random.randint (1,100)
					DELTA = current_performance - new_performance
					TEMP = T_MAX - TIME
					accept_prob = (math.e**(-alpha*(float(DELTA)/TEMP)))*100
					if(randProb < accept_prob):
						current_Maze = new_maze
						current_performance = new_performance
				TIME += 1
			else:
				prob -=0.01
		return current_Maze



