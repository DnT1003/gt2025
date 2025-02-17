import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    """
    Creates and returns a graph with predefined edges.
    """
    G = nx.Graph()
    edges = [(1, 2), (2, 5), (6, 3), (4, 6), (4, 7), (6, 7)]
    G.add_edges_from(edges)
    return G

def path_existence(graph, node1, node2):
    """
    Check if a path exists between two nodes in the graph.
    Args:
        graph (nx.Graph): The graph to check.
        node1 (int): The first node.
        node2 (int): The second node.
    Returns:
        bool: True if a path exists, False otherwise.
    """
    try:
        return nx.has_path(graph, node1, node2)
    except nx.NetworkXError:
        return False

def draw_graph_with_path(graph, node1, node2):
    """
    Draws the graph and highlights the path between two nodes if it exists.
    Args:
        graph (nx.Graph): The graph to visualize.
        node1 (int): The starting node.
        node2 (int): The target node.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph, seed=42)

    # Draw the entire graph
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)

    if nx.has_path(graph, node1, node2):
        # Highlight the shortest path
        path = nx.shortest_path(graph, source=node1, target=node2)
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='red', width=2)
        print(f"Path exists: {' -> '.join(map(str, path))}")
    else:
        print(f"No path exists between node {node1} and node {node2}.")

    plt.title(f"Graph Visualization with Path from {node1} to {node2}")
    plt.show()

def main():
    """
    Main function to execute the graph visualization and path checking.
    """
    graph = create_graph()

    try:
        node1 = int(input("Enter the first node (1-7): "))
        node2 = int(input("Enter the second node (1-7): "))

        if node1 not in graph.nodes or node2 not in graph.nodes:
            print("One or both nodes are not present in the graph. Please enter valid nodes.")
            return

        draw_graph_with_path(graph, node1, node2)
    except ValueError:
        print("Invalid input. Please enter integer values for the nodes.")

if __name__ == "__main__":
    main()