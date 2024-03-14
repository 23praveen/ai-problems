import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

def astar(start_state, goal_state, heuristic_func, successor_func):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic_func(start_state, goal_state))
    heapq.heappush(open_list, (start_node.total_cost(), id(start_node), start_node))

    while open_list:
        _, _, current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for successor_state, step_cost in successor_func(current_node.state):
            if successor_state in closed_set:
                continue

            new_cost = current_node.cost + step_cost
            new_heuristic = heuristic_func(successor_state, goal_state)
            new_node = Node(successor_state, current_node, new_cost, new_heuristic)
            heapq.heappush(open_list, (new_node.total_cost(), id(new_node), new_node))

    return None

# Example heuristic function (Euclidean distance)
def euclidean_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Example successor function (4-connected grid)
def successors(state):
    x, y = state
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 10 and 0 <= new_y < 10:  # Assuming a 10x10 grid
            yield ((new_x, new_y), 1)  # Step cost of 1

# Example usage:
start = (0, 0)
goal = (9, 9)
path = astar(start, goal, euclidean_distance, successors)
print("A* Path:", path)
