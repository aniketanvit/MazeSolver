from random import randint
import math

class simulateAnnealing:
	# Possible directions in an array
	x = [0,0,1,-1]
    y = [1,-1,0,0]

    old_cost = math.inf
    new_cost = 0
    best = []
    accept_prob = 0
    path = []
    fringe_stack = []

    def directions(cx,cy, gx,gy, fringe_stack):
    	## this isn't nessacarily random, figure out how to make it random 
    	for i in range(0,4,1):
            row = cx + x[i]
            col = cy +y[i]
            if(row >= 0 and row < gx and col >= 0 and col < gy):
                if maze[row][col] == 0:
                    fringe_queue.append([row,col])

        print(fringe_queue)

    def search_algo_dfs(maze, sx,sy, gx,gy):
    	start = maze[sx][sy]
    	fringe_stack.append([sx,sy])
    	path[:] = []
    	fringe_stack[:] = []
        #print(fringe_stack)
        while fringe_stack:
            current_state = fringe_stack.pop()
            maze[current_state[0]][current_state[1]] = 5
            #print(current_state)
            cx = current_state[0]
            cy = current_state[1]
            if cx == gx and cy == gy :
                print("Reached Goal")
                path.append(current_state)
                return path
            directions(cx,cy,gx,gy,fringe_stack)
            path.append(current_state)
            #print(fringe_stack)
        return -1

    def simulate_annealing(maze, sx,sy, gx,gy):
    	while True:## not sure what the convergence factor will be
    		i =1
    		while i <= 100:
    			new_path = search_algo_dfs(maze, sx, sy, gx, gy)
    			if(new_path == -1):
    				print "UNSOLVABLE"
    				break;
    			new_cost = len(new_path)
    			if(new_cost < old_cost):
    				best = path;
    				old_cost = new_cost
    			else:
    				accept_prob = math.e**(old_cost-new_cost)/t
					prob = random(0,1)
					if(prob < accept_prob):
					 	best = path
					 	old_cost = new_cost
				i+=1
				# t needs to change for the accpet_prob to go down
		return best, old_cost

	def searchHardestPath(maze, sx,sy, gx,gy):
		best, new_cost = simulate_annealing(maze, sx,sy, gx,gy)
		## still working on this
		return hardestMaze

