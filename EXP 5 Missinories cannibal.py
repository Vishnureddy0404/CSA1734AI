from collections import deque

def is_valid(state):
    m, c, _ = state
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if (m < c and m > 0) or ((3 - m) < (3 - c) and (3 - m) > 0):
        return False
    return True

def get_successors(state):
    m, c, b = state
    if b == 1:
        possible_moves = [(-1, 0, 0), (-2, 0, 0), (0, -1, 0), (0, -2, 0), (-1, -1, 0)]
    else:
        possible_moves = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]
    
    successors = []
    for move in possible_moves:
        new_state = (m + move[0], c + move[1], 1 - b)
        if is_valid(new_state):
            successors.append(new_state)
    
    return successors

def solve(start, goal):
    frontier = deque([start])
    explored = set()
    parent_map = {start: None}
    
    while frontier:
        state = frontier.popleft()
        
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent_map[state]
            return path[::-1]
        
        explored.add(state)
        
        for successor in get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
                parent_map[successor] = state
    
    return None

def main():
    print("Missionaries and Cannibals Problem")
    missionaries = int(input("Enter the number of missionaries: "))
    cannibals = int(input("Enter the number of cannibals: "))
    
    start = (missionaries, cannibals, 1)
    goal = (0, 0, 0)
    
    if missionaries != 3 or cannibals != 3:
        print("This program is designed to work with exactly 3 missionaries and 3 cannibals.")
        return
    
    solution = solve(start, goal)
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
