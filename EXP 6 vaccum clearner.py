from collections import deque

class Environment:
    def __init__(self, grid, start_pos):
        self.grid = grid
        self.start_pos = start_pos
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_dirty(self, pos):
        x, y = pos
        return self.grid[x][y] == 'D'

    def clean(self, pos):
        x, y = pos
        self.grid[x][y] = 'C'

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 'O'

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = environment.start_pos

    def move(self, new_pos):
        if self.environment.is_valid(new_pos):
            self.position = new_pos
            return True
        return False

    def clean(self):
        if self.environment.is_dirty(self.position):
            self.environment.clean(self.position)

def bfs_clean_all(environment):
    start_pos = environment.start_pos
    queue = deque([(start_pos, [])])
    visited = set()
    visited.add(start_pos)

    while queue:
        position, path = queue.popleft()
        if environment.is_dirty(position):
            environment.clean(position)
            path.append(position)

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (position[0] + move[0], position[1] + move[1])
            if new_pos not in visited and environment.is_valid(new_pos):
                visited.add(new_pos)
                queue.append((new_pos, path + [new_pos]))

    return path

def main():
    # User input for grid size
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    # User input for grid configuration
    grid = []
    start_pos = None
    print("Enter the grid configuration (use 'C' for clean, 'D' for dirty, 'O' for obstacle, and 'V' for vacuum start):")
    for i in range(rows):
        row = input().strip().split()
        for j in range(cols):
            if row[j] == 'V':
                start_pos = (i, j)
                row[j] = 'C'  # Treat the starting position as clean
        grid.append(row)

    # Initialize environment and vacuum cleaner
    environment = Environment(grid, start_pos)
    vacuum_cleaner = VacuumCleaner(environment)

    # Display initial grid
    print("Initial grid:")
    environment.display_grid()

    # Clean all dirty spots using BFS
    path = bfs_clean_all(environment)

    # Display final grid
    print("Final grid:")
    environment.display_grid()

    # Output the sequence of moves
    print("Sequence of moves:")
    for pos in path:
        print(f"Moved to: {pos}")

if __name__ == "__main__":
    main()
