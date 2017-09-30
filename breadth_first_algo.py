def directions(cx,cy, gx,gy, fringe_queue):
    #possible directions
    east = cy + 1
    west = cy - 1
    north = cx - 1
    south = cx + 1
    if cx < gx and east < gy and cx >= 0 and east >= 0:
        if maze[cx][east] == 0:
            fringe_queue.append([cx,east])

    else:
        pass
    if  cx < gx and west < gy and cx >= 0 and west >= 0:
        if maze[cx][west] == 0:
            fringe_queue.append([cx,west])
    else:
        pass
    if  north < gx and cy < gy and north >= 0 and cy >=0:
        if maze[north][cy] == 0:
            fringe_queue.append([north,cy])
    else:
         pass
    if  south < gx and cy < gy and south >= 0 and cy >= 0:
        if maze[south][cy] == 0:
            fringe_queue.append([south,cy])
    else:
         pass
    print(fringe_queue)


def search_algo_bfs(maze, sx,sy, gx,gy):
    start = maze[sx][sy]
    path = []
    fringe_queue_queue = []
    fringe_queue.append([sx,sy])
    print(fringe_queue)
    while fringe_queue:
        current_state = fringe_queue.pop(0)
        maze[current_state[0]][current_state[1]] = 5
        print(current_state)
        cx = current_state[0]
        cy = current_state[1]
        if cx == gx and cy == gy :
            print("Reached Goal")
            path.append(current_state)
            return path
        directions(cx,cy,gx,gy,fringe_queue)
        path.append(current_state)
        print(fringe_queue)
    return path
