from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent
    
    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    
    def successors(self):
        children = []
        if self.boat == 1:
            for i in range(3):
                for j in range(3):
                    if 1 <= i + j <= 2:
                        new_state = State(self.missionaries - i, self.cannibals - j, 0, self)
                        if new_state.is_valid():
                            children.append(new_state)
        else:
            for i in range(3):
                for j in range(3):
                    if 1 <= i + j <= 2:
                        new_state = State(self.missionaries + i, self.cannibals + j, 1, self)
                        if new_state.is_valid():
                            children.append(new_state)
        return children

def bfs_search():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    
    queue = deque([initial_state])
    visited = set()
    visited.add((initial_state.missionaries, initial_state.cannibals, initial_state.boat))
    
    while queue:
        state = queue.popleft()
        for child in state.successors():
            if (child.missionaries, child.cannibals, child.boat) not in visited:
                if child.is_goal():
                    return child
                queue.append(child)
                visited.add((child.missionaries, child.cannibals, child.boat))
    
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append((solution.missionaries, solution.cannibals, solution.boat))
        solution = solution.parent
    path.reverse()
    for idx, state in enumerate(path):
        if state[2] == 1:
            print(f"Step {idx + 1}: {state[0]} Missionaries, {state[1]} Cannibals | Boat: Left to Right")
        else:
            print(f"Step {idx + 1}: {state[0]} Missionaries, {state[1]} Cannibals | Boat: Right to Left")
    print()

if __name__ == "__main__":
    solution = bfs_search()
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
