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
        # graph_class.Vertex.__init__(self, vertex_id, edges)
        super().__init__(vertex_id, edges)
        for node_number in range(len(self._node_id)):
            self._node_id[node_number] = [self._node_id[node_number], False]

    def mark_explored(self):
        """
        Marks node as explored
        """
        for node in self.get_nodes():
            node[1] = True

    def mark_unexplored(self):
        """
        Marks node as unexplored
        """
        for node in self.get_nodes():
            node[1] = False

    def explored_value(self):
        """
        returns boolean as to whether node is explored
        """
        return self.get_nodes()[1]

    def __repr__(self):
        """printable list of nodes and edges for the object"""
        return "Node: " + str(self._node_id) + " Edge: " \
               + str(self._edge_list)


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
    search_queue.append(start_vertex)
    start_vertex.mark_explored()
    while len(search_queue) > 0:
        active_node = search_queue.pop(0)
        for edge in active_node.get_edges():
            linked_vertex = graph.get_vertex(edge)
            if not linked_vertex.get_nodes()[0][1]:
                linked_vertex.mark_explored()
                search_queue.append(linked_vertex)


def create_graph(graph_data):
    """
    create graph class object from file
    """
    new_graph = BfsGraph()
    for item in range(len(graph_data)):
        new_graph.create_vertex(graph_data[item][0][0])
        for edge in range(len(graph_data[item][1])):
            new_graph.get_vertex(
                graph_data[item][0][0]).add_edge(graph_data[item][1][edge])
    return new_graph


test_graph_data = [[[1], [2, 3, 5]],
                   [[2], [1, 2]],
                   [[3], [1, 4, 5]],
                   [[4], [3, 5]],
                   [[5], [1, 3, 4]]]


if __name__ == '__main__':
    test_graph = create_graph(test_graph_data)
    print(str(test_graph))
    print('run bfs')
    bfs(test_graph, 1)
    print(str(test_graph))
