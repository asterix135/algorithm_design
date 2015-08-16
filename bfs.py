"""
Simple breadth first search function
"""

import graph_class


class BfsVertex(graph_class.Vertex):
    """
    Minor class adjustments to make BFS work better
    """

    def __init__(self, vertex_id, edges=None):
        """
        Adapt base class setup to make _node_id a list of lists:
        [[node_id, explored],...]
        """
        graph_class.Vertex.__init__(self, vertex_id, edges)
        for node_number in range(len(self._node_id)):
            self._node_id[node_number] = [node_number, False]

    def mark_explored(self):
        """
        Marks node as explored
        """
        for node in self.get_nodes():
            node[1] = True


class BfsGraph(graph_class.Graph):
    """
    minor class adjustments to make this work better
    """

    def create_vertex(self, key):
        """
        creates a new vertex and returns that vertex
        """
        new_vertex = BfsVertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex


def bfs(graph, start_node=1):
    """Basic BFS function"""
    search_queue = []
    start_vertex = graph.get_vertex(start_node)
    search_queue.append(graph.get_vertex(start_vertex))
    start_vertex.mark_explored()
    while len(search_queue) > 0:
        active_node = search_queue.pop(0)
        for edge in active_node.get_edges():
            linked_vertex = graph.get_vertex(edge)
            if not graph.get_vertex(linked_vertex)[1]:
                linked_vertex.mark_explored()
                search_queue.append(linked_vertex)


def create_graph(graph_data):
    """
    create graph class object from file
    """
    new_graph = BfsGraph()
    for item in range(len(graph_data)):
        for edge in range(len(graph_data[item][1])):
            new_graph.add_edge(graph_data[item][0], graph_data[item][1][edge])
    return new_graph


test_graph_data = [[[1], [2, 3, 5]],
                   [[2], [1, 2]],
                   [[3], [1, 4, 5]],
                   [[4], [3, 5]],
                   [[5], [1, 3, 4]]]


test_graph = create_graph(test_graph_data)
print(str(test_graph))
print('run bfs')
bfs(test_graph, 1)
