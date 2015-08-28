"""
Graph Class for Kosaraju's Algorithm
"""

import graph_class_new

# TODO: 2) Think about how to have the graph class keep track of sorts


class KjVertex(graph_class_new.Vertex):
    """
    Vertex class for Graph
    """

    def __init__(self, vertex_id, edges=None):
        """
        Vertex takes two parameters - vertex_id and optional edges
        both are lists
        initializes node_id, edge list, explored value, finishing time
        & leader
        """
        super().__init__(vertex_id, edges)
        self._explored = False
        self._finishing_time = 0
        self._leader = 0

    def __repr__(self):
        """debug representation"""
        expl = "explored" if self._explored else "unexplored"
        return "Node " + str(self._node_id) + expl + " finish " + \
               str(self._finishing_time) + " leader " + str(self._leader)

    def __str__(self):
        """printable list of nodes and edges for the object"""
        return "Node: " + str(self._node_id) + ", Explored: " + \
               str(self._explored) + ", Finish time: " + \
               str(self._finishing_time) + ", Leader: " + str(self._leader) + \
               "\n  Edge: " + str(self._edge_list)

    def mark_explored(self):
        """Marks vertex as explored"""
        self._explored = True

    def mark_unexplored(self):
        """Marks vertex as unexplored"""
        self._explored = False

    def is_explored(self):
        """Returns boolean _explored value"""
        return self._explored

    def set_finishing_time(self, time_value):
        """sets finishing time value"""
        self._finishing_time = time_value

    def get_finishing_time(self):
        """returns finishing time value"""
        return self._finishing_time

    def set_leader(self, leader_value):
        """sets value of leader"""
        self._leader = leader_value

    def get_leader(self):
        """returns leader value"""
        return self._leader


class KjGraph(graph_class_new.Graph):
    """
    Modifications to basic Graph Class
    """

    def create_vertex(self, key):
        """
        creates a new vertex of KjVertex class and returns that vertex
        """
        new_vertex = KjVertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex

    def reverse_graph(self):
        """
        reverses a directed graph and returns reversed graph
        for undirected graph, just returns self
        """
        if self._type == 'u':
            return self
        reversed_graph = KjGraph('d')
        for vertex in self:
            for edge in vertex.get_edges():
                reversed_graph.add_edge(edge, vertex.get_node_id())
        return reversed_graph


def create_kj_graph(graph_data):
    """
    creates a new Graph based on input data
    data needs to be in format [[vertex_id, [edge list]], etc...]
    """
    new_graph = KjGraph('d')
    for item in range(len(graph_data)):
        new_graph.create_vertex(graph_data[item][0])
        for edge in range(len(graph_data[item][1])):
            new_graph.get_vertex(
                graph_data[item][0]).add_edge(graph_data[item][1][edge])
    return new_graph

if __name__ == '__main__':
    test_graph = [[1, [2]],
                  [2, [3]],
                  [3, [1, 4]],
                  [4, [5]],
                  [5, [6]],
                  [6, [4]]]

    test_graph = create_kj_graph(test_graph)
    print(str(test_graph))
    reverse_graph = test_graph.reverse_graph()
    print(str(reverse_graph))
