# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 07:23:18 2017

@author: Gaurav Ahlawat
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:33:18 2017

@author: Gaurav Ahlawat
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:19:03 2017

@author: Gaurav Ahlawat
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:03:18 2017

@author: Gaurav Ahlawat
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:02:13 2017

@author: Gaurav Ahlawat
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:14:24 2017

@author: Gaurav Ahlawat
"""

import random
import matplotlib.pyplot as plt 
import copy

def getNewMaze (ROWLEN, COLLEN, cell_blocked_probalility):
    grid = []
    MAXNUM = cell_blocked_probalility * 100
    MAXROW = ROWLEN
    MAXCOL = COLLEN

    for row in range (0, MAXROW, 1):
        rw = []
        for col in range (0, MAXCOL, 1):
            rand = random.randint (1, 100)
            if (rand < MAXNUM):
                rw.append(3)
            else:
                rw.append(2)
        grid.append (rw)
    grid[0][0] = 0
    grid[MAXROW - 1][MAXCOL - 1] = 0
    return grid

import math
import heapq

def adjacent_cells_manhattan(cx,cy, gx,gy, parent,cost_till,open, maze):
    #possible directions
    cells = []
    cost_man = {}
    cost_euc = {}
    east = cy + 1
    west = cy - 1
    north = cx - 1
    south = cx + 1
    if cx < gx and east < gy and cx >= 0 and east >= 0:
        if maze[cx][east] == 2 and [cx,east] not in open:
            parent[cx,east] = [cx,cy]
            cost_man[cx,east] = manhattan_dist(cx, east, gx, gy)
            #cost_euc[cx,east] = euclidean_dist(cx, east, gx, gy)
            cost_till[cx, east] = cost_till[cx, cy] + 1 + cost_man[cx,east]
            cost1 = cost_man[cx,east]
            cells.append([cx,east, cost1])
    if  cx < gx and west < gy and cx >= 0 and west >= 0:
        if maze[cx][west] == 2 and [cx,west] not in open:
            parent[cx,west] = [cx,cy]
            cost_man[cx,west] = manhattan_dist(cx, west, gx, gy)
            #cost_euc[cx,west] = euclidean_dist(cx, west, gx, gy)
            cost_till[cx, west] = cost_till[cx, cy] + 1 + cost_man[cx,west]
            cost2 = cost_man[cx,west]
            cells.append([cx,west,cost2])
    if  north < gx and cy < gy and north >= 0 and cy >=0:
        if maze[north][cy] == 2 and [north,cy] not in open:
            parent[north,cy] = [cx, cy]
            cost_man[north,cy] = manhattan_dist(north, cy, gx, gy)
            #cost_euc[north,cy] = euclidean_dist(north, cy, gx, gy)
            cost_till[north, cy] = cost_till[cx, cy] + 1 + cost_man[north,cy]
            cost3 = cost_man[north,cy]
            cells.append([north,cy,cost3])
    if  south < gx and cy < gy and south >= 0 and cy >= 0:
        if maze[south][cy] == 2 and [south,cy] not in open:
            parent[south,cy] = [cx, cy]
            cost_man[south,cy] = manhattan_dist(south, cy, gx, gy)
            #cost_euc[south,cy] = euclidean_dist(south, cy, gx, gy)
            cost_till[south, cy] = cost_till[cx, cy] + 1 + cost_man[south,cy]
            cost4 = cost_man[south,cy]
            cells.append([south,cy,cost4])
    """
    Sorting based on the Euclidean distance from the neighbours to the goal
    """
    from operator import itemgetter
    cells = sorted(cells, key = itemgetter(2), reverse = True)
    #print(cells)
    #print(cells)
    return cells, parent

def adjacent_cells_euclidean(cx,cy, gx,gy, parent,cost_till,open, maze):
    #possible directions
    cells = []
    cost_man = {}
    cost_euc = {}
    east = cy + 1
    west = cy - 1
    north = cx - 1
    south = cx + 1
    if cx < gx and east < gy and cx >= 0 and east >= 0:
        if maze[cx][east] == 2 and [cx,east] not in open:
            parent[cx,east] = [cx,cy]
            #cost_man[cx,east] = manhattan_dist(cx, east, gx, gy)
            cost_euc[cx,east] = euclidean_dist(cx, east, gx, gy)
            cost_till[cx, east] = cost_till[cx, cy] + 1 + cost_euc[cx,east]
            cost1 = cost_euc[cx,east]
            cells.append([cx,east, cost1])
    if  cx < gx and west < gy and cx >= 0 and west >= 0:
        if maze[cx][west] == 2 and [cx,west] not in open:
            parent[cx,west] = [cx,cy]
            #cost_man[cx,west] = manhattan_dist(cx, west, gx, gy)
            cost_euc[cx,west] = euclidean_dist(cx, west, gx, gy)
            cost_till[cx, west] = cost_till[cx, cy] + 1 + cost_euc[cx,west]
            cost2 = cost_euc[cx,west]
            cells.append([cx,west,cost2])
    if  north < gx and cy < gy and north >= 0 and cy >=0:
        if maze[north][cy] == 2 and [north,cy] not in open:
            parent[north,cy] = [cx, cy]
            #cost_man[north,cy] = manhattan_dist(north, cy, gx, gy)
            cost_euc[north,cy] = euclidean_dist(north, cy, gx, gy)
            cost_till[north, cy] = cost_till[cx, cy] + 1 + cost_euc[north,cy]
            cost3 = cost_euc[north,cy]
            cells.append([north,cy,cost3])
    if  south < gx and cy < gy and south >= 0 and cy >= 0:
        if maze[south][cy] == 2 and [south,cy] not in open:
            parent[south,cy] = [cx, cy]
            #cost_man[south,cy] = manhattan_dist(south, cy, gx, gy)
            cost_euc[south,cy] = euclidean_dist(south, cy, gx, gy)
            cost_till[south, cy] = cost_till[cx, cy] + 1 + cost_euc[south,cy]
            cost4 = cost_euc[south,cy]
            cells.append([south,cy,cost4])
    """
    Sorting based on the Euclidean distance from the neighbours to the goal
    """
    from operator import itemgetter
    cells = sorted(cells, key = itemgetter(2), reverse = True)
    #print(cells)
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

def path(sx, sy, cx, cy, parent):
    ## Constantly poping Key errors
    #print("Tracking the path taken where cx: %d  and cy: %d" %(cx,cy))
    path_1 = []
    path_1.append([cx,cy])
    #print(parent)
    while parent[cx,cy] != [sx,sy]:
        cx, cy = parent[cx, cy]
        #print('path: Cell: %d, %d' % (cx, cy))
        path_1.append([cx,cy])
        #print(path_1)
        #print(len(path_1))
    return len(path_1)
        


def search_algo_astar_manhattan(maze,sx,sy,gx,gy,count):
    open = []
    count = 0
    closed = []
    parent = {}
    heapq.heappush(open,[sx,sy])
    cost_till = {}
    cost_till[sx,sy] = 0
    parent[sx,sy] = None
    while open:
        #print(open)
        cell = open.pop()
        #count += 1
        #print(cell[0])
        #print(cell[1])
        #print(cell)
        maze[cell[0]][cell[1]] = 5
        #print(maze)
        closed.append(cell)
        neighbors, parents = adjacent_cells_manhattan(cell[0],cell[1],gx,gy,parent,cost_till,open, maze)
        parent.update(parents)
        for neighbor in neighbors:
            if neighbor not in closed:
                #print(neighbor)
                #print(rep)
                #heapq.heappush(open,[neighbor[0],neighbor[1]])
                open.append(neighbor)
                count += 1
            #print(parent[cell[0],cell[1]])
        if cell[0] == (gx-1) and cell[1] == (gy -1):
            #return count
            #return path(sx,sy,cell[0],cell[1],parent)
            return maze
        #print(parent)
    return("Goal not found")

def search_algo_astar_euclidean(maze,sx,sy,gx,gy,count):
    open = []
    count = 0
    closed = []
    parent = {}
    heapq.heappush(open,[sx,sy])
    cost_till = {}
    cost_till[sx,sy] = 0
    parent[sx,sy] = None
    while open:
        #print(open)
        cell = open.pop()
        #count += 1
        #print(cell[0])
        #print(cell[1])
        #print(cell)
        maze[cell[0]][cell[1]] = 5
        #print(maze)
        closed.append(cell)
        neighbors, parents = adjacent_cells_euclidean(cell[0],cell[1],gx,gy,parent,cost_till,open, maze)
        parent.update(parents)
        for neighbor in neighbors:
            if neighbor not in closed:
                #print(neighbor)
                #print(rep)
                #heapq.heappush(open,[neighbor[0],neighbor[1]])
                open.append(neighbor)
                count += 1
            #print(parent[cell[0],cell[1]])
        if cell[0] == (gx-1) and cell[1] == (gy -1):
            return maze
            #return path(sx,sy,cell[0],cell[1],parent)
            #return maze
        #print(parent)
    return("Goal not found")

def main():
    maze1 = getNewMaze(20,20,0.2)
    maze2 = getNewMaze(20,20,0.2)
    maze_out_1 = search_algo_astar_euclidean(maze1,0,0,20,20,0)
    maze_out_2 = search_algo_astar_manhattan(maze2,0,0,20,20,0)


if __name__ == '__main__':
    main()