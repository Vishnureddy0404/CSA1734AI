from collections import deque

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_quantity):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_quantity = target_quantity
        self.visited = set()
    
    def solve(self):
        queue = deque([(0, 0)])  # Start with both jugs empty
        self.visited.add((0, 0))
        
        while queue:
            current_state = queue.popleft()
            jug1, jug2 = current_state
            
            # Check if target quantity is reached
            if jug1 == self.target_quantity or jug2 == self.target_quantity or jug1 + jug2 == self.target_quantity:
                print(f"Target quantity of {self.target_quantity} liters can be measured.")
                return True
            
            # Define all possible operations
            next_states = []
            
            # Fill jug1
            next_states.append((self.jug1_capacity, jug2))
            
            # Fill jug2
            next_states.append((jug1, self.jug2_capacity))
            
            # Empty jug1
            next_states.append((0, jug2))
            
            # Empty jug2
            next_states.append((jug1, 0))
            
            # Pour jug1 to jug2
            pour_amount = min(jug1, self.jug2_capacity - jug2)
            next_states.append((jug1 - pour_amount, jug2 + pour_amount))
            
            # Pour jug2 to jug1
            pour_amount = min(jug2, self.jug1_capacity - jug1)
            next_states.append((jug1 + pour_amount, jug2 - pour_amount))
            
            # Explore each next state
            for state in next_states:
                if state not in self.visited:
                    queue.append(state)
                    self.visited.add(state)
        
        print(f"Target quantity of {self.target_quantity} liters cannot be measured.")
        return False

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_quantity = 2
    
    problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_quantity)
    problem.solve()
