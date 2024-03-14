def water_jug_problem(jug1_cap, jug2_cap, target_amount):
    """Solves the Water Jug Problem using Breadth-First Search (BFS)"""

    # Initialize jugs with 0 water
    jug1 = 0
    jug2 = 0

    # Actions: fill, empty a jug, or pour from one to the other
    actions = [
        ("fill", 1), ("fill", 2), 
        ("empty", 1), ("empty", 2), 
        ("pour", 1, 2), ("pour", 2, 1)
    ]

    # Track visited states (jug1, jug2) to prevent loops
    visited = set()

    # Queue for BFS: stores (jug1, jug2, sequence of actions)
    queue = [(jug1, jug2, [])]

    while queue:
        jug1, jug2, actions_taken = queue.pop(0)  # Dequeue state

        # Goal: find if a jug contains the target amount
        if jug1 == target_amount or jug2 == target_amount:
            return actions_taken

        # Skip already visited states
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))  # Mark as visited

        # Generate possible next states based on actions
        for action in actions:
            if action[0] == "fill":
                if action[1] == 1:
                    next_state = (jug1_cap, jug2)
                else:
                    next_state = (jug1, jug2_cap)

            elif action[0] == "empty":
                if action[1] == 1:
                    next_state = (0, jug2)
                else:
                    next_state = (jug1, 0)

            else:  # "pour" action
                jug_from, jug_to = action[1:]
                amount = min(eval(f"jug{jug_from}"), eval(f"jug{jug_to}_cap") - eval(f"jug{jug_to}"))
                next_state = (
                    eval(f"jug{jug_from}") - amount, 
                    eval(f"jug{jug_to}") + amount
                )

            # If the new state is valid and unvisited, add to queue
            if next_state not in visited:
                queue.append((next_state[0], next_state[1], actions_taken + [action]))

    # No solution found
    return None

# Get input
jug1_capacity = int(input("Enter capacity of jug 1: "))
jug2_capacity = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

# Solve and print steps
solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")