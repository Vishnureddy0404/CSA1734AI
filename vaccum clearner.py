import random

class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (random.randint(0, 4), random.randint(0, 4))  # Random initial position
    
    def print_environment(self):
        for row in self.environment:
            print(row)
        print()
    
    def clean(self):
        cleaned = 0
        while cleaned < 25:
            x, y = self.position
            if self.environment[x][y] == 1:
                print(f"Cleaning position ({x}, {y})")
                self.environment[x][y] = 0
                cleaned += 1
            self.print_environment()
            self.move()
    
    def move(self):
        x, y = self.position
        if x % 2 == 0:  # Even row
            if y < 4:
                y += 1
            else:
                x += 1
        else:  # Odd row
            if y > 0:
                y -= 1
            else:
                x += 1
        self.position = (x, y)

if __name__ == "__main__":
    # Initialize the environment (5x5 grid with random dirty cells)
    environment = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    
    print("Initial Environment:")
    for row in environment:
        print(row)
    print()
    
    cleaner = VacuumCleaner(environment)
    print("Starting cleaning process:")
    cleaner.clean()
    print("Cleaning completed. Final Environment:")
    for row in environment:
        print(row)
