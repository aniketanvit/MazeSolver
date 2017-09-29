from enums import CellState


class SearchAlgorithms:
    def __init__ (self, maze):
        self.maze = maze
        self.start_x = 0
        self.start_y = 0
        self.goal_x = len (maze) - 1
        self.goal_y = len (maze[0]) - 1

    def breadth_first_search (self, maze):
        fringe = Queue ()
        return self._search (fringe)

    def depth_first_search (self, maze):
        fringe = Stack ()
        return self._search (fringe)

    def a_star_manhattan (self, fringe, ):
        pass

    def _search (self, fringe):
        fringe.push ([self.start_x, self.start_y])
        while (fringe.is_empty () == False):
            current_state = fringe.pop ()
            cx = current_state[0]
            cy = current_state[1]
            self.maze[cx][cy] = CellState.VISITED.value

            if ((cx == self.goal_x) and (cy == self.goal_y)):
                return True
            self._expand_state (cx, cy, self.goal_x, self.goal_y, fringe)
        return False

    def _heuristic_search (self, fringe, heuristic):
        start = self.maze[self.start_x][self.start_y]
        fringe.push ([self.start_x, self.start_y])
        while (fringe.is_empty () == False):
            current_state = fringe.pop ()
            self.maze[current_state[0]][current_state[1]] = 5
            cx = current_state[0]
            cy = current_state[1]
            if (cx == self.goal_x and cy == self.goal_y):
                return True
            self._expand_state (cx, cy, self.goal_x, self.goal_y, fringe)
        return False

    def _expand_state (self, cx, cy, gx, gy, fringe):
        # all possible directions
        east = cy + 1
        west = cy - 1
        north = cx - 1
        south = cx + 1

        if ((east <= gy) and (self.maze[cx][east] != CellState.VISITED.value) and (
            self.maze[cx][east] != CellState.BLOCKED.value)):
            fringe.push ([cx, east])

            # if ((west >= 0) and (self.maze[cx][east] != CellState.VISITED.value) and (self.maze[cx][east] != CellState.BLOCKED.value)):
            # fringe.push ([cx, west])

            # if ((north >= 0) and (self.maze[cx][east] != CellState.VISITED.value) and (self.maze[cx][east] != CellState.BLOCKED.value)):
            # fringe.push ([north, cy])

        if ((south <= gx) and (self.maze[south][cy] != CellState.VISITED.value) and (
            self.maze[south][cy] != CellState.BLOCKED.value)):
            fringe.push ([south, cy])

    def manhattan_distance (self, a, b, c, d):
        return abs (a - c) + abs (b - d)

    def euclidean_distance (self, a, b, c, d):
        xd = a - c
        yd = b - d
        ## Isn't the eudlicean distance Math.sqrt(Math.pow(x2-x1,2) + Math.pow(y2-y1,2)) ? 
        return (xd * xd) + (yd * yd)

    def dummy_heuristic (self, a, b, c, d):
        return 0


class Cell:
    def __init__ (self, r, c):
        self.row = r
        self.col = c


class Stack:
    def __init__ (self):
        self.stack = []

    def pop (self):
        if self.is_empty ():
            return None
        else:
            return self.stack.pop ()

    def push (self, val):
        return self.stack.append (val)

    def peak (self):
        if self.is_empty ():
            return None
        else:
            return self.stack[-1]

    def size (self):
        return len (self.stack)

    def is_empty (self):
        return self.size () == 0


class Queue:
    def __init__ (self):
        self.queue = []

    def push (self, val):
        self.queue.insert (0, val)

    def pop (self):
        if self.is_empty ():
            return None
        else:
            return self.queue.pop ()

    def size (self):
        return len (self.queue)

    def is_empty (self):
        return self.size () == 0
