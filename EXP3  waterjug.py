from collections import deque

def is_valid_state(state, jug1_capacity, jug2_capacity):
    return 0 <= state[0] <= jug1_capacity and 0 <= state[1] <= jug2_capacity

def bfs(jug1_capacity, jug2_capacity, target_amount):
    start_state = (0, 0)  # Both jugs are initially empty
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    
    while queue:
        (jug1, jug2), path = queue.popleft()
        
        if jug1 == target_amount or jug2 == target_amount:
            return path + [(jug1, jug2)]
        
        next_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1))),  # Pour jug2 into jug1
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug1 + jug2, jug2_capacity))   # Pour jug1 into jug2
        ]
        
        for state in next_states:
            if is_valid_state(state, jug1_capacity, jug2_capacity) and state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))
    
    return None

def main():
    jug1_capacity = int(input("Enter the capacity of jug 1: "))
    jug2_capacity = int(input("Enter the capacity of jug 2: "))
    target_amount = int(input("Enter the target amount of water: "))
    
    result = bfs(jug1_capacity, jug2_capacity, target_amount)
    
    if result:
        print("Solution found:")
        for state in result:
            print(f"Jug 1: {state[0]}L, Jug 2: {state[1]}L")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
