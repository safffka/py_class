import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_planar_graph(num_vertices, num_edges):
    if num_edges < num_vertices - 1 or num_edges > num_vertices * (num_vertices - 1) / 2:
        raise ValueError("Invalid number of edges for the given number of vertices.")

    G = nx.Graph()

    coordinates = {i: (random.random(), random.random()) for i in range(num_vertices)}

    G.add_nodes_from(coordinates.keys())

    possible_edges = [(i, j) for i in range(num_vertices) for j in range(i)]

    random.shuffle(possible_edges)

    for edge in possible_edges:
        if not creates_edge_crossing(G, edge, coordinates):
            G.add_edge(*edge)

        if G.number_of_edges() == num_edges:
            break

    if G.number_of_edges() != num_edges:
        raise ValueError("Unable to generate a planar graph with the given number of vertices and edges.")

    visualize_graph(G, coordinates)


def creates_edge_crossing(G, new_edge, coordinates):
    for edge in G.edges():
        if do_edges_cross(new_edge, edge, coordinates):
            return True
    return False


def do_edges_cross(edge1, edge2, coordinates):
    a, b = coordinates[edge1[0]], coordinates[edge1[1]]
    c, d = coordinates[edge2[0]], coordinates[edge2[1]]
    return not (a == c or a == d or b == c or b == d) and intersect(a, b, c, d)


def intersect(p, q, r, s):
    return orientation(p, q, r) != orientation(p, q, s) and orientation(r, s, p) != orientation(r, s, q)


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def visualize_graph(G, coordinates):
    plt.figure(figsize=(8, 8))

    nx.draw_networkx_nodes(G, coordinates, node_size=200, node_color='lightblue')

    nx.draw_networkx_edges(G, coordinates, width=2, alpha=0.5)

    nx.draw_networkx_labels(G, coordinates, font_size=10, font_color='black')

    plt.axis('off')
    plt.title('Planar Graph Visualization')
    plt.show()


generate_planar_graph(4, 5)
