"""modification of bfs to calculate shortest path"""

import bfs, graph_class


class SpVertex(bfs.BfsVertex):
    """Minor class adjustments for shortest path"""

    def __init__(self, vertex_id, edges=None):
        """
        Initialize _node_id as a 3-part list [id, explored, distance]
        """
        super().__init__(vertex_id, edges)
        for node_number in range(len(self._node_id)):
            self._node_id[node_number] += [float('inf')]

    def update_distance(self, new_distance):
        """Update distance in node_id"""
        self._node_id[0][2] = new_distance


class SpGraph(graph_class.Graph):
    """
    amend class to create vertex using SpVertex class
    """

    def create_vertex(self, key):
        """
        creates a new vertex and returns that vertex
        """
        new_vertex = SpVertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex


def shortest_path(graph, start_node=1):
    """
    takes graph and start node as input
    for each vertex, calculates shortest past from start node
    update vertex's node_id to include distance
    """
    search_queue = []
    start_vertex = graph.get_vertex(start_node)
    start_vertex.update_distance(0)
    search_queue.append(start_vertex)
    start_vertex.mark_explored()
    while len(search_queue) > 0:
        active_node = search_queue.pop(0)
        for edge in active_node.get_edges():
            linked_vertex = graph.get_vertex(edge)
            if not linked_vertex.get_nodes()[0][1]:
                linked_vertex.mark_explored()
                linked_vertex.update_distance(active_node.get_nodes()[0][2] + 1)
                search_queue.append(linked_vertex)


def create_graph(graph_data):
    """
    create graph class object from file
    """
    new_graph = SpGraph()
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
    shortest_path(test_graph, 1)
    print(str(test_graph))
