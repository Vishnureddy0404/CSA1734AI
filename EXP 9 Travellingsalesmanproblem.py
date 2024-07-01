from itertools import permutations

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[i + 1]]
    total_distance += distance_matrix[permutation[-1]][permutation[0]]  # return to the starting city
    return total_distance

def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_distance = float('inf')
    best_permutation = None
    
    for permutation in permutations(cities):
        current_distance = calculate_total_distance(permutation, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_permutation = permutation
            
    return best_permutation, min_distance

def main():
    print("Travelling Salesman Problem")
    num_cities = int(input("Enter the number of cities: "))
    
    distance_matrix = []
    print("Enter the distance matrix row by row (separated by spaces):")
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        distance_matrix.append(row)
    
    best_permutation, min_distance = travelling_salesman(distance_matrix)
    
    print("Optimal route:", best_permutation)
    print("Minimum distance:", min_distance)

if __name__ == "__main__":
    main()
