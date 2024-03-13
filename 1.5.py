def is_valid_state(missionaries, cannibals, boat_side):
    """Checks if the current state is valid."""
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False  # Invalid number of people
    if missionaries < cannibals and missionaries > 0:
        return False  # Cannibals outnumber missionaries on either side
    return True

def solve_missionaries_cannibals(missionaries, cannibals, boat_side, visited_states=None):
    """Solves the Missionaries and Cannibals problem recursively with state tracking."""
    if visited_states is None:
        visited_states = set()  # Initialize visited states set

    if missionaries == 0 and cannibals == 0 and boat_side == "right":
        return True  # Goal state reached

    current_state = (missionaries, cannibals, boat_side)
    if current_state in visited_states:
        return False  # Already visited this state

    visited_states.add(current_state)  # Mark current state as visited

    for m in range(2):  # Try moving 0, 1, or 2 missionaries
        for c in range(2):  # Try moving 0, 1, or 2 cannibals
            if m + c > 0 and m + c <= 2:  # At least one person must move, and max 2
                new_missionaries = missionaries - m if boat_side == "left" else missionaries + m
                new_cannibals = cannibals - c if boat_side == "left" else cannibals + c
                new_boat_side = "right" if boat_side == "left" else "left"

                if is_valid_state(new_missionaries, new_cannibals, new_boat_side):
                    if solve_missionaries_cannibals(new_missionaries, new_cannibals, new_boat_side, visited_states):
                        print(f"Move {m} missionaries and {c} cannibals to the {new_boat_side}.")
                        return True

    return False  # No valid move found

# Initial state
missionaries = 3
cannibals = 3
boat_side = "left"

if solve_missionaries_cannibals(missionaries, cannibals, boat_side):
    print("Solution found!")
else:
    print("No solution exists.")