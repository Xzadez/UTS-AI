import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def dijkstra(self, start, goal):
        queue = [(0, start)]
        visited = set()
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous_vertices = {}
        
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            
            if current_vertex == goal:
                path = []
                while current_vertex in previous_vertices:
                    path.insert(0, current_vertex)
                    current_vertex = previous_vertices[current_vertex]
                return path, distances[goal]
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    previous_vertices[neighbor] = current_vertex
        
        return distances[goal]
    
def print_map(grid):
    for row in grid:
        print(" ".join(row))

def main():
    # Define the map
    map_grid = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', 'G', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    # Create a copy of the map before finding the shortest path
    map_grid_before = [row[:] for row in map_grid]
    
    # Create a graph
    graph = Graph()
    for i in range(len(map_grid)):
        for j in range(len(map_grid[0])):
            if map_grid[i][j] != '#':
                edges = {}
                if i > 0 and map_grid[i-1][j] != '#':
                    edges[(i-1, j)] = 1
                if i < len(map_grid)-1 and map_grid[i+1][j] != '#':
                    edges[(i+1, j)] = 1
                if j > 0 and map_grid[i][j-1] != '#':
                    edges[(i, j-1)] = 1
                if j < len(map_grid[0])-1 and map_grid[i][j+1] != '#':
                    edges[(i, j+1)] = 1
                graph.add_vertex((i, j), edges)
    
    # Find the shortest path using Dijkstra's algorithm
    start = (1, 1)
    goal = (3, 3)
    path, distance = graph.dijkstra(start, goal)
    
    # Mark the shortest path on the map
    for node in path:
        x, y = node
        if map_grid[x][y] != 'S' and map_grid[x][y] != 'G':
            map_grid[x][y] = '-'
    
    # Print the map before finding the shortest path
    print("Sebelum ditemukan jalur terpendek")
    for row in map_grid_before:
        print(" ".join(row))
    
    # Print the map after finding the shortest path
    print("\nSetelah ditemukan jalur terpendek")
    print_map(map_grid)

if __name__ == "__main__":
    main()
