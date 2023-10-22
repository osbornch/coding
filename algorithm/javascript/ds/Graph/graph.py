class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class Graph:
    def __init__(self):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes)

    def construct_graph(self, nodes):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                graph[edge][node] = graph[node][edge]

graph = Graph()

print("Hello world")