"""
Topological Sort implementation
"""

import bfs

class TsVertex(bfs.BfsVertex):
    """Changes to base graph class to make algo work"""

    def add_label(self, label):
        """Add label to node_id"""
        self._node_id[0].append(label)


class TsGraph(bfs.BfsGraph):
    def create_vertex(self, key):
        """
        creates a new vertex and returns that vertex
        """
        new_vertex = TsVertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex


def topo_search(graph):
    """
    Takes a directed graph as input and sorts it such that for every edge,
    the sort number of the tail is less than the sort number of the head

    Pseudocode:
    # DFS - Loop (graph G)
    # - mark all nodes unexplored
    # - current_label = n (count down as explored - to keep track of ordering)
    # - for each vertex v in G
    #          - if v not yet explored in some prevous DFS call
    #                DFS - (G, v)
    #                     at end of DFS (NOT DFS -loop) - if nowhere else to go
    #                          set f(s) = current value
    #                          current_value -= 1
    """

    current_label = len(graph)

    def dfs(graph, start_node):
        """
        Takes graph & start vertex as parameters
        explores graph with DFS approach
        """
        nonlocal current_label
        start_vertex = graph.get_vertex(start_node)
        start_vertex.mark_explored()
        for edge in start_vertex.get_edges():
            linked_vertex = graph.get_vertex(edge)
            if not linked_vertex.get_nodes()[0][1]:
                dfs(graph, edge)
        start_vertex.add_label(current_label)
        current_label -= 1

    def dfs_loop(graph):
        """
        outer function call for topological search
        """
        for vertex in graph:
            vertex.mark_unexplored()
        for vertex in graph:
            if not vertex.get_nodes()[0][1]:
                dfs(graph, vertex.get_nodes()[0][0])
        return graph

    dfs_loop(graph)


def construct_graph(graph_data):
    new_graph = TsGraph('d')
    for item in range(len(graph_data)):
        new_graph.create_vertex(graph_data[item][0][0])
        for edge in range(len(graph_data[item][1])):
            new_graph.get_vertex(
                graph_data[item][0][0]).add_edge(graph_data[item][1][edge])
    return new_graph


test_graph_data = [[[7], [8, 11]],
                   [[5], [11]],
                   [[3], [8, 10]],
                   [[11], [2, 9, 10]],
                   [[8], [9]],
                   [[2], []],
                   [[9], []],
                   [[10], []]]


if __name__ == '__main__':
    test_graph = construct_graph(test_graph_data)
    print('original: ' + str(test_graph) + '\n')
    sorted_graph = topo_search(test_graph)
    print('sorted: ' + str(test_graph))