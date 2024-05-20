import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Define the grid size
rows, cols = 20, 20

# Define the grid (1: blocked, 0: open)
grid = np.zeros((rows, cols), dtype=int)

# Adding some blocked cells (1 represents a blocked cell)
blocked_cells = [
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
    (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9),
    (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (18, 5), (19, 5),
    (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14)
]
for cell in blocked_cells:
    grid[cell] = 1

# Starting points (A and T) and target point (X)
start_A = (19, 19)
start_T = (0, 0)
target = (0, 10)

# Define directions for moving in the grid
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start, target):
    queue = deque([start])
    visited = set()
    visited.add(start)
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if neighbor not in visited and grid[neighbor] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current
    path = []
    if target in came_from:
        while target:
            path.append(target)
            target = came_from[target]
        path.reverse()
    return path

# Get shortest paths
path_A = bfs(grid, start_A, target)
path_T = bfs(grid, start_T, target)

# Plot the grid
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xticks(np.arange(0.5, cols, 1))
ax.set_yticks(np.arange(0.5, rows, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)

# Fill in the blocked cells
for r in range(rows):
    for c in range(cols):
        if grid[r, c] == 1:
            ax.add_patch(plt.Rectangle((c, r), 1, 1, color='black'))

# Mark the start and target points
ax.add_patch(plt.Rectangle(start_A[::-1], 1, 1, color='blue', label='A = Andi'))
ax.add_patch(plt.Rectangle(start_T[::-1], 1, 1, color='red', label='T = Tika'))
ax.add_patch(plt.Rectangle(target[::-1], 1, 1, color='green', label='X = Taman'))

# Plot the paths
for (r, c) in path_A:
    ax.add_patch(plt.Circle((c + 0.5, r + 0.5), 0.2, color='blue', alpha=0.6))

for (r, c) in path_T:
    ax.add_patch(plt.Circle((c + 0.5, r + 0.5), 0.2, color='red', alpha=0.6))

# Display the grid
plt.gca().invert_yaxis()
plt.legend(loc='upper right')
plt.show()
