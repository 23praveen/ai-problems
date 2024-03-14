from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v):
        visited = set()
        stack = [v]

        while stack:
            s = stack.pop()
            if s in visited:
                continue

            visited.add(s)
            print(s, end=' ')

            for neighbor in self.graph[s]:
                stack.append(neighbor)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print('Depth First Search:')
    g.dfs(2)