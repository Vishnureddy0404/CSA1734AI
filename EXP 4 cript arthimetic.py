import itertools
def solve_cryptarithmetic(puzzle):
    words, result = puzzle.split(' = ')
    words = words.split(' + ')
    unique_letters = set(''.join(words) + result)
    assert len(unique_letters) <= 10, "Too many unique letters"

    for perm in itertools.permutations('0123456789', len(unique_letters)):
        table = str.maketrans(''.join(unique_letters), ''.join(perm))
        if all(word[0] != '0' for word in words + [result]):
            if sum(int(word.translate(table)) for word in words) == int(result.translate(table)):
                return {ch: int(digit) for ch, digit in zip(unique_letters, perm)}
    return None
def main():
    puzzle = input("Enter the cryptarithmetic puzzle : ")
    solution = solve_cryptarithmetic(puzzle)
    
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
