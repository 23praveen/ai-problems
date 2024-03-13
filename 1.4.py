from itertools import permutations

def is_valid(word1, word2, result, char_map):
    """Checks if the given mapping satisfies the cryptarithmetic equation."""
    num1 = int("".join(str(char_map[c]) for c in word1))
    num2 = int("".join(str(char_map[c]) for c in word2))
    num_result = int("".join(str(char_map[c]) for c in result))
    return num1 + num2 == num_result and (char_map[word1[0]] != 0 and char_map[word2[0]] != 0 and char_map[result[0]] != 0)

def solve_cryptarithmetic(word1, word2, result):
    """Solves the cryptarithmetic problem using backtracking."""
    unique_chars = set(word1 + word2 + result)
    for perm in permutations(range(10), len(unique_chars)):
        char_map = dict(zip(unique_chars, perm))
        if is_valid(word1, word2, result, char_map):
            return char_map
    return None  # No solution found
word1 = "SEND"
word2 = "MORE"
result = "MONEY"

solution = solve_cryptarithmetic(word1, word2, result)

if solution:
    print("Solution:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")