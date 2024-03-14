import itertools

def tsp_brute_force(graph):
    num_nodes = len(graph)
    # Generate all possible permutations of node indices
    permutations = itertools.permutations(range(1, num_nodes))
    min_cost = float('inf')
    optimal_path = None

    for perm in permutations:
        # Form the complete tour by adding the starting and ending node
        tour = (0,) + perm + (0,)
        # Calculate the cost of the tour
        cost = calculate_tour_cost(tour, graph)
        # Update the minimum cost and optimal path if a better solution is found
        if cost < min_cost:
            min_cost = cost
            optimal_path = tour

    return optimal_path, min_cost

def calculate_tour_cost(tour, graph):
    cost = 0
    for i in range(len(tour) - 1):
        # Accumulate the cost of each edge in the tour
        cost += graph[tour[i]][tour[i + 1]]
    return cost

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
optimal_path, min_cost = tsp_brute_force(graph)
print("Optimal path:", optimal_path)
print("Minimum cost:", min_cost)
