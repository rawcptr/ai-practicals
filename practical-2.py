import heapq


class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid  # 2D grid where 0 = walkable, 1 = blocked
        self.start = start  # Start position (x, y)
        self.goal = goal  # Goal position (x, y)
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, node):
        # Manhattan distance heuristic
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def neighbors(self, node):
        # Return valid neighbors (up, down, left, right)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: right, down, left, up
        result = []
        for d in dirs:
            neighbor = (node[0] + d[0], node[1] + d[1])
            if (
                0 <= neighbor[0] < self.rows
                and 0 <= neighbor[1] < self.cols
                and self.grid[neighbor[0]][neighbor[1]] == 0
            ):
                result.append(neighbor)
        return result

    def search(self):
        # Priority queue to store (f_score, node)
        open_list = []
        heapq.heappush(open_list, (0, self.start))

        came_from = {}  # For reconstructing path
        g_score = {self.start: 0}  # Cost from start to each node
        f_score = {
            self.start: self.heuristic(self.start)
        }  # Estimated cost from start to goal

        while open_list:
            current = heapq.heappop(open_list)[1]

            # If we reached the goal, reconstruct the path
            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g_score = (
                    g_score[current] + 1
                )  # Distance from current to neighbor is 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update the best path to the neighbor
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return []  # Return empty path if no solution

    def reconstruct_path(self, came_from, current):
        # Reconstruct path from came_from dictionary
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Reverse path to start from the beginning


# 0 = walkable, 1 = blocked
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0, 0)  # Starting position
goal = (4, 4)  # Goal position

a_star = AStar(grid, start, goal)
path = a_star.search()

print("Path from start to goal:", path)
