from random import randint
import math
x = [0,0,1,-1]
y = [1,-1,0,0]

best = []
accept_prob = 0
path = []
fringe_queue = []

def printMaze(maze):
	for i in range(0, len(maze)-1):
		for j in range(0,len(maze)-1):
			print maze[i][j],
		print

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

def directions(maze,cx,cy, gx,gy, fringe_queue): 
	for i in range(0,4,1):
		row = cx + x[i]
		col = cy +y[i]
		if(row >= 0 and row < gx and col >= 0 and col < gy):
			if maze[row][col] == 0:
				fringe_queue.append([row,col])

       #print(fringe_queue)

def search_algo_bfs(maze, sx,sy, gx,gy):
	start = maze[sx][sy]
	path[:] = []
	fringe_queue[:] = []
	fringe_queue.append([sx,sy])
	#print(fringe_queue)
	while fringe_queue:
		current_state = fringe_queue.pop(0)
		maze[current_state[0]][current_state[1]] = 5
		#print(current_state)
		cx = current_state[0]
		cy = current_state[1]
		if cx == gx and cy == gy :
			print("Reached Goal")
			path.append(current_state)
			return len(path)
		directions(maze,cx,cy,gx,gy,fringe_queue)
		path.append(current_state)
		#print(fringe_queue)
	return -1

class simulateAnnealing:
	# Possible directions in an array
	def simulate_annealing_hard_maze(self,maze,sx,sy,gx,gy,prob):
		current_Maze = maze
		current_performance = search_algo_bfs(maze, sx,sy, gx,gy)
		printMaze(current_Maze) ## for testing determing if it really does get better
		if current_performance == -1:
			print "UNSOLVABLE.. start with a map that is SOLVABLE"
			return
		alpha = 0.9
		T_MAX = 50
		TIME = 1
		## start loop
		while(TIME < T_MAX):
			prob += 0.01 ## change maze slightly
			new_maze = generate2DMaze(20, prob)# generate new maze
			new_performance = search_algo_dfs(new_maze, sx,sy, gx,gy)
			if(new_performance != -1): ## ignore maze's without solutions
				if(new_performance > current_performance):
					current_Maze = new_maze
				else:
					prob = random(0,1)
					DELTA = current_performance - new_performance
					TEMP = T_MAX - TIME
					accept_prob = math.e**(-alpha*(float(DELTA)/TEMP))
					if(prob < accept_prob):
						current_Maze = new_maze
				TIME += 1
			else:
				prob -=0.01
		return current_Maze



