from naiwny import naive_strongly_connected_components
from kosaraju import kosaraju_strongly_connected_components
from random import *

def __init__(self, nodes_start, nodes_end, edges_start, edges_end, nodes_step, edges_step,
             algorithm, loop ):
    self.nodes_start = nodes_start
    self.nodes_end = nodes_end
    self.edges_start = edges_start
    self.edges_end = edges_end
    self.nodes_step = nodes_step
    self.edges_step = edges_step
    self.algorithm = algorithm
    self.loop = loop

class Graph(object):

    def experiment(nodes_start, nodes_end, edges_start, edges_end, nodes_step, edges_step,
             algorithm, loop ):

        graph = Graph(nodes_start, nodes_end, edges_start, edges_end,
                      nodes_step, edges_step, algorithm, loop)

        for nodes in range(nodes_start, nodes_end, nodes_step):
            S, T = set(nodes), set()

            current_node = random.sample(S, 1).pop()
            S.remove(current_node)
            T.add(current_node)

            # Utworzenie randomowo polaczonego grafu.
            while S:
                next_node = random.sample(nodes, 1).pop()
                if next_node not in T:
                    edge = (current_node, next_node )
                    graph.add_edge(edge)
                    S.remove(next_node)
                    T.add(next_node)
                current_node = next_node
            graph.add_random_edges(next_node)

            if algorithm == "kosaraju":
                kosaraju_strongly_connected_components(graph)
            else:
                naive_strongly_connected_components(graph)