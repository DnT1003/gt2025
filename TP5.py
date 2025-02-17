import sys

def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    previous = [-1] * n

    distance[source] = 0

    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_node = min((i for i in range(n) if not visited[i]), key=lambda i: distance[i], default=-1)

        if min_node == -1 or distance[min_node] == sys.maxsize:  # No reachable nodes left
            break

        visited[min_node] = True

        # Update distances for neighbors of the current node
        for neighbor in range(n):
            if graph[min_node][neighbor] != float('inf') and not visited[neighbor]:
                new_dist = distance[min_node] + graph[min_node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = min_node

    return distance, previous

def reconstruct_path(previous, target):
    path = []
    current = target
    while current != -1:
        path.append(current)
        current = previous[current]
    return path[::-1]

def main():
    # Graph adjacency matrix representation
    graph = [
        [0, 4, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
        [4, 0, float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), float('inf')],
        [1, float('inf'), 0, 8, float('inf'), 7, float('inf'), float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), 8, 0, float('inf'), float('inf'), float('inf'), 5, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), 2, 2, float('inf')],
        [float('inf'), 3, 7, float('inf'), 1, 0, float('inf'), 1, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 3, 4, 4],
        [float('inf'), float('inf'), float('inf'), 5, 2, 1, 3, 0, 6, 7],
        [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, 6, 0, 1],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4, 7, 1, 0]
    ]

    # Node labels
    nodes = "ABCDEFGHLM"

    # Input source and target
    source_label = input("Enter source node (e.g., A): ").strip().upper()
    target_label = input("Enter target node (e.g., M): ").strip().upper()

    if source_label not in nodes or target_label not in nodes:
        print("Invalid nodes. Please enter valid node labels.")
        return

    source = nodes.index(source_label)
    target = nodes.index(target_label)

    # Run Dijkstra's algorithm
    distance, previous = dijkstra(graph, source)

    # Reconstruct and display the shortest path
    path = reconstruct_path(previous, target)
    path_labels = [nodes[i] for i in path]

    # Output results
    if distance[target] == sys.maxsize:
        print(f"No path exists between {source_label} and {target_label}.")
    else:
        print("Shortest path:", " -> ".join(path_labels))
        print("Total weight of shortest path:", distance[target])

if __name__ == "__main__":
    main()

