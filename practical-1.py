from collections import defaultdict, deque


class Graph:
    def __init__(self):
        # Use defaultdict for adjacency list representation
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph, add reverse edge

    def dfs_recursive(self, vertex, visited=None):
        if visited is None:
            visited = set()  # Initialize visited set on the first call

        # Mark the current node as visited and print it
        visited.add(vertex)
        print(vertex, end=" ")

        # Recur for all adjacent vertices not yet visited
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)  # Pass the same visited set

    def bfs(self, start):
        visited = set()  # Keep track of visited nodes
        q = deque([start])  # Initialize queue with the starting node
        visited.add(start)  # Mark the start node as visited

        while q:
            # Dequeue a vertex from the front of the queue
            vertex = q.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)


# --- Usage Example ---
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Expected Graph Structure:
# 0 -- 1
# |  /
# 2 -- 3 -- 4

print("Depth First Search (starting from vertex 0):")
g.dfs_recursive(0)
# Possible valid DFS outputs (order depends on neighbour list order):
# 0 1 2 3 4
# 0 2 1 3 4
# etc.

print("\n\nBreadth First Search (starting from vertex 0):")
g.bfs(0)
# Expected BFS output (order within a level might vary):
# 0 1 2 3 4
