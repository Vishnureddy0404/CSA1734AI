from itertools import permutations

def is_valid_solution(letters, digits):
    s, e, n, d, m, o, r, y = digits
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    return send + more == money

def solve_crypt_arithmetic():
    letters = 'SENDMORE'
    for digits in permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = digits
        if s != 0 and m != 0:  # Ensure no leading zeros
            if is_valid_solution(letters, digits):
                return {letters[i]: digits[i] for i in range(len(letters))}

    return None

def main():
    solution = solve_crypt_arithmetic()
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
