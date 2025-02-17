from collections import defaultdict

def dfs(graph, node, visited, result=None):
    """
    Depth-First Search to traverse and collect nodes.
    :param graph: Adjacency matrix representing the graph
    :param node: Current node to visit
    :param visited: List tracking visited nodes
    :param result: List to store traversal order or SCC
    """
    visited[node] = True
    if result is not None:
        result.append(node + 1)  # Convert to 1-based index
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def kosaraju_scc(graph):
    """
    Find Strongly Connected Components (SCCs) using Kosaraju's Algorithm.
    :param graph: Adjacency matrix representing the graph
    :return: List of SCCs
    """
    n = len(graph)
    visited = [False] * n
    stack = []

    # Step 1: Perform DFS and push nodes to stack in finishing order
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    # Step 2: Transpose the graph
    transpose = [[graph[j][i] for j in range(n)] for i in range(n)]

    # Step 3: Perform DFS on the transposed graph in stack order
    visited = [False] * n
    sccs = []

    while stack:
        node = stack.pop() - 1  # Convert to 0-based index
        if not visited[node]:
            scc = []
            dfs(transpose, node, visited, scc)
            sccs.append(scc)

    return sccs

def find_wccs(graph):
    """
    Find Weakly Connected Components (WCCs) using DFS.
    :param graph: Adjacency matrix representing the graph
    :return: List of WCCs
    """
    n = len(graph)
    visited = [False] * n
    wccs = []

    for i in range(n):
        if not visited[i]:
            wcc = []
            dfs(graph, i, visited, wcc)
            wccs.append(wcc)

    return wccs

if __name__ == "__main__":
    # Input graph (adjusted adjacency matrix without node 0)
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0]
    ]

    # Find SCCs and WCCs
    sccs = kosaraju_scc(G)
    wccs = find_wccs(G)

    # Output the results with 1-based indexing
    print("Strongly Connected Components (SCCs):")
    for idx, scc in enumerate(sccs):
        print(f"SCC {idx + 1}: {scc}")

    print("\nWeakly Connected Components (WCCs):")
    for idx, wcc in enumerate(wccs):
        print(f"WCC {idx + 1}: {wcc}")
