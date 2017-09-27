from enums import MazeState


class MazeSolver:
    def __init__ (self, search_algorithms):
        self.search_algorithms = search_algorithms

    def solve_with_dfs (self, maze):
        success = self.search_algorithms.depth_first_search (maze)
        if (success):
            self.maze_state = MazeState.SOLVED
        else:
            self.maze_state = MazeState.UNSOLVABLE

        return self.maze_state

    def solve_with_bfs (self, maze):
        success = self.search_algorithms.breadth_first_search (maze)
        if (success):
            self.maze_state = MazeState.SOLVED
        else:
            self.maze_state = MazeState.UNSOLVABLE

        return self.maze_state

    def solve_with_astar (self, maze):
        success = self.search_algorithms.astar_search (maze)
        if (success):
            self.maze_state = MazeState.SOLVED
        else:
            self.maze_state = MazeState.UNSOLVABLE

        return self.maze_state
