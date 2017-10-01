"""
Problem with returning the parent and costs from the function
Simply move the calculcation of parent and the heuristic costs to the loop inside the solving function and update the values as we go on
This way we can update the value and also wouldn't have to worry about the changing values being passed to the different functions
"""

"""
Change the way the cells are being added to the Open list
It should be kind of DFS, but importance is given the Euclidean distance here
"""
import math
import heapq
class aStarAlgorMan:
    x = [0,0,1,-1]
    y = [1,-1,0,0]

    def adjacent_cells(cx,cy, gx,gy, parent,cost_till,open):
        #possible directions
        cells = []
        cost_man = {}
        cost_euc = {}
        #east = cy + 1
        #west = cy - 1
        #north = cx - 1
        #south = cx + 1
        #if cx < gx and east < gy and cx >= 0 and east >= 0:
            #if maze[cx][east] == 0 and [cx,east] not in open:
                #parent[cx,cy] = [cx,east]
                #cost_man[cx,east] = manhattan_dist(cx, east, gx, gy)
                #cost_till[cx, east] = cost_till[cx, cy] + 1 + cost_man[cx,east]
                #cost1 = cost_man[cx,east]
                #cells.append([cx,east, cost1])
        #if  cx < gx and west < gy and cx >= 0 and west >= 0:
            #if maze[cx][west] == 0 and [cx,west] not in open:
                #parent[cx,cy] = [cx,west]
                #cost_man[cx,west] = manhattan_dist(cx, west, gx, gy)
                #cost_till[cx, west] = cost_till[cx, cy] + 1 + cost_man[cx,west]
                #cost2 = cost_man[cx,west]
                #cells.append([cx,west,cost2])
        #if  north < gx and cy < gy and north >= 0 and cy >=0:
            #if maze[north][cy] == 0 and [north,cy] not in open:
                #parent[cx,cy] = [north, cy]
                #cost_man[north,cy] = manhattan_dist(north, cy, gx, gy)
                #cost_till[north, cy] = cost_till[cx, cy] + 1 + cost_man[north,cy]
                #cost3 = cost_man[north,cy]
                #cells.append([north,cy,cost3])
        #if  south < gx and cy < gy and south >= 0 and cy >= 0:
            #if maze[south][cy] == 0 and [south, cy] not in open:
                #parent[south,cy] = [south, cy]
                #cost_man[south,cy] = manhattan_dist(south, cy, gx, gy)
                #cost_till[south, cy] = cost_till[cx, cy] + 1 + cost_man[south,cy]
                #cost4 = cost_man[south,cy]
                #cells.append([south,cy,cost4])
        for i in range(0,4,1):
            row = cx + x[i]
            col = cy +y[i]
            if(row >= 0 and row < gx and col >= 0 and col < gy):
                if maze[row][col] == 0 and [row,col] not in open:
                    parent[cx,cy] = [row,col]
                    cost_man[row,col] = manhattan_dist(row, col, gx, cy)
                    cost_till[row,col] = cost_till[cx, cy] + 1 + cost_man[row,col]
                    cost1 = cost_man[row,col]
                    cells.append([row,col, cost1])

    """
    Sorting based on the Euclidean distance from the neighbours to the goal
    """
    from operator import itemgetter
    cells = sorted(cells, key = itemgetter(2), reverse = True)
    print(cells)
    #print(cells)
    return cells, parent


    def manhattan_dist(cx, cy, gx, gy):
        return abs((gx-cx-1) + (gy-cy-1))

    def euclidean_dist(cx,cy,gx,gy):
        return abs(math.sqrt((cx - (gx-1))**2 + (cy - (gy-1))**2))

    def update_cell(n, cell):
        n.g = cell.g + 10
        n.h = manhattan_dist(n[0],n[1])
        n.parent = cell
"""
def path(sx, sy, cx, cy, parent):
    ## Constantly poping Key errors
    #print("Tracking the path taken where cx: %d  and cy: %d" %(cx,cy))
    while parent[cx,cy] != [sx,sy]:
        cx, cy = parent[cx, cy]
        #print('path: Cell: %d, %d' % (cx, cy))
"""

    import heapq
    def search_algo_astar(maze,sx,sy,gx,gy):
        open = []
        rep = 0
        closed = []
        parent = {}
        heapq.heappush(open,[sx,sy])
        cost_till = {}
        cost_till[sx,sy] = 0
        parent[sx,sy] = None
        while open:
            #print(open)
            cell = open.pop()
            #print(cell[0])
            #print(cell[1])
            #print(cell)
            maze[cell[0]][cell[1]] = 5
            #print(maze)
            closed.append(cell)
            neighbors, parents = adjacent_cells(cell[0],cell[1],gx,gy,parent,cost_till,open)
            parent.update(parents)
            for neighbor in neighbors:
                if neighbor not in closed:
                    #print(neighbor)
                    #print(rep)
                    #heapq.heappush(open,[neighbor[0],neighbor[1]])
                    open.append(neighbor)
                    #print(parent[cell[0],cell[1]])
            if cell[0] == (gx-1) and cell[1] == (gy -1):
                #return path(sx,sy,cell[0],cell[1],parent)
                return maze
                #print(parent)
        return("Goal not found")
