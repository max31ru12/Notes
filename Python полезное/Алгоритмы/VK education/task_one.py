from collections import deque

graph = {
        'A': ['M', 'P'],
        'M': ['A', 'N'],
        'N': ['M', 'B'],
        'P': ['A', 'B'],
        'B': ['P', 'N'],
        }


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {'start': None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    return visited


print(bfs('A', 'B', graph))
