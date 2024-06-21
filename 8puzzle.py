import heapq

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.n = 3  # size of the puzzle

    def solve(self):
        def get_neighbors(state):
            neighbors = []
            zero_idx = state.index(0)
            zero_row, zero_col = divmod(zero_idx, self.n)

            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for move in moves:
                new_row, new_col = zero_row + move[0], zero_col + move[1]
                if 0 <= new_row < self.n and 0 <= new_col < self.n:
                    new_idx = new_row * self.n + new_col
                    new_state = list(state)
                    new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
                    neighbors.append(tuple(new_state))

            return neighbors

        def heuristic(state):
            dist = 0
            for idx, value in enumerate(state):
                if value != 0:
                    goal_idx = self.goal.index(value)
                    dist += abs(idx // self.n - goal_idx // self.n) + abs(idx % self.n - goal_idx % self.n)
            return dist

        open_set = []
        heapq.heappush(open_set, (0 + heuristic(self.start), 0, self.start, None))

        closed_set = set()
        came_from = {}

        while open_set:
            _, cost, current, parent = heapq.heappop(open_set)
            if current in closed_set:
                continue

            came_from[current] = parent

            if current == self.goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            closed_set.add(current)

            for neighbor in get_neighbors(current):
                if neighbor in closed_set:
                    continue
                heapq.heappush(open_set, (cost + 1 + heuristic(neighbor), cost + 1, neighbor, current))

        return None

def print_puzzle(state):
    n = int(len(state) ** 0.5)
    for i in range(n):
        print(state[i * n:(i + 1) * n])
    print()

if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 5, 6, 7, 8)  # starting state of the puzzle
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)   # goal state of the puzzle

    puzzle = Puzzle(start, goal)
    solution = puzzle.solve()

    if solution:
        print("Solution found in {} steps:".format(len(solution) - 1))
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution found.")
