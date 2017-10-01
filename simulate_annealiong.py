from random import randint
class simulateAnnealing:
	# Possible directions in an array
	x = [0,0,1,-1]
    y = [1,-1,0,0]
    visitedNeighbors = {}
    path = []
    oldSolutionCount = 0

	## Add all possible neighbors to the stack
	def directions(cx,cy, gx,gy, fringe_queue):
		for i in range(0,4,1):
			row = cx + x[i]
			col = cy +y[i]
			if(row >= 0 && row < gx && col >= 0 && col < gy):
				if maze[row][col] == 0:
					fringe_queue.append([row,col])
			#print(fringe_queue)

	## Generate a random solution using depth first search (may not neccasarily be optimal)
	def dfs(maze, sx,sy, gx,gy):
		start = maze[sx][sy]
		path = []
		fringe_stack = []
		fringe_stack.append([sx,sy])
		while fringe_stack:
			current = fringe_stack.pop()
			if maze[current[0],current[1]] is not 3 and maze[current[0],current[1]] is not 4:
				cx = current[0]
				cy = current[1]
				if cx == gx and cy == gy :
					print("SOLVABLE")
					path.append(current)
					visitedNeighbors.add(current)
					return path
				directions(cx,cy,gx,gy,fringe_stack)
				path.append(current)
				visitedNeighbors.add(current)
				oldSolutionCount += 1
		return -1

	## Generate random solution other than we have visited
	def generateRandomNeighbor(cx,cy, gx,gy, fringe_queue):
		generateRandom = []
		for i in range(0,4,1):
			row = cx + x[i]
			col = cy + y[i]
			generateRandom.append([row,col])
		while True:
			random = randint(0,3)
			if(generateRandom[random] not in visitedNeighbors):
				randomRow = generateRandom[random][0]
				randomCOl = generateRandom[random][1]
				break
		return [randomRow,randomCOl]

	def simulateAnnealing(maze, sx,sy, gx,gy):
		path = dfs(maze, sx,sy, gx,gy)
		if(path == -1):
			print "UNSOLVABLE"
			return
		parentToGoal = path[len(path)-2]
		parent = generateRandomNeighbor(parentToGoal[0], parentToGoal[1], gx, gy, fringe_queue)
		## generateed solution called parent(parent to goal)
		## not sure how to calculate the new solutions cost
		## Next stop is comparing the new solution and only take an old solution
		## based on some probability, repeat these steps till we converge or find a better solution




