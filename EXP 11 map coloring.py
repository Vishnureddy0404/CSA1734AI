def is_valid(assignment, state, color, neighbors):
    """Check if the current color assignment is valid."""
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_variable(assignment, variables):
    """Select an unassigned variable to assign next."""
    for variable in variables:
        if variable not in assignment:
            return variable
    return None

def backtrack(assignment, variables, domains, neighbors):
    """Backtracking algorithm to solve CSP."""
    if len(assignment) == len(variables):
        return assignment

    state = select_unassigned_variable(assignment, variables)

    for color in domains[state]:
        if is_valid(assignment, state, color, neighbors):
            assignment[state] = color
            result = backtrack(assignment, variables, domains, neighbors)
            if result:
                return result
            assignment.pop(state)

    return None

def map_coloring(variables, domains, neighbors):
    """Solve the map coloring problem using backtracking CSP algorithm."""
    assignment = {}
    return backtrack(assignment, variables, domains, neighbors)

# Example usage
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {
    'WA': ['Red', 'Green', 'Blue'],
    'NT': ['Red', 'Green', 'Blue'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q': ['Red', 'Green', 'Blue'],
    'NSW': ['Red', 'Green', 'Blue'],
    'V': ['Red', 'Green', 'Blue'],
    'T': ['Red', 'Green', 'Blue']
}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

solution = map_coloring(variables, domains, neighbors)
print("Solution:", solution)
