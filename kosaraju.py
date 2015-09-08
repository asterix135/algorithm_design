"""
Kosaraju's Algorithm for finding Strongly Connected Components
"""

import graph_class_kosaraju as gc


def kosaraju(graph):
    """
    runs kosaraju's algorithim on a directed graph to calculate
    strongly connected components
    takes graph as input and modifies that graph
    """
    rev_graph = graph.reverse_graph()
    time_value = 0
    start_value = None
    pass1_order = list(graph.get_vertices())
    pass1_order.sort(reverse=True)
    pass2_order = []

    def dfs(graph_dfs, node):
        """modified depth-first search"""
        nonlocal time_value, start_value
        start_vertex = graph_dfs.get_vertex(node)
        start_vertex.mark_explored()
        start_vertex.set_leader(start_value)
        for edge in start_vertex.get_edges():
            linked_vertex = graph_dfs.get_vertex(edge)
            if not linked_vertex.is_explored():
                dfs(graph_dfs, edge)
        time_value += 1
        start_vertex.set_finishing_time(time_value)
        pass2_order.insert(0, start_vertex.get_node_id())

    def dfs_non_recursive(graph_dfs, node):
        """modified, non-recursive dfs to prevent stack overflow problems"""
        nonlocal time_value, start_value
        search_stack = []
        start_vertex = graph_dfs.get_vertex(node)
        search_stack.append(start_vertex)
        start_vertex.mark_explored()
        start_vertex.set_leader(start_value)
        while len(search_stack) > 0:
            active_node = search_stack.pop()
            for edge in active_node.get_edges():
                linked_vertex = graph_dfs.get_vertex(edge)
                if not linked_vertex.is_explored:
                    linked_vertex.mark_explored()
                    search_stack.append(linked_vertex)
        time_value += 1
        start_vertex.set_finishing_time(time_value)
        pass2_order.insert(0, start_vertex.get_node_id())


    def dfs_loop(graph_loop, order_list):
        """main outer loop for algorithm"""
        nonlocal start_value
        for node in graph_loop:
            node.mark_unexplored()
        for vertex_number in order_list:
            node = graph_loop.get_vertex(vertex_number)
            if not node.is_explored():
                start_value = node.get_node_id()
                # dfs(graph_loop, start_value)
                dfs_non_recursive(graph_loop, start_value)
        return graph

    dfs_loop(rev_graph, pass1_order)
    pass2_copy = pass2_order.copy()
    dfs_loop(graph, pass2_copy)


if __name__ == '__main__':
    test_graph = [[1, [2]],
                  [2, [3]],
                  [3, [1, 4]],
                  [4, [5]],
                  [5, [6]],
                  [6, [4]]]

    # test_graph = [[1, [2]],
    #               [2, [3, 4, 5]],
    #               [3, [6]],
    #               [4, [7, 5]],
    #               [5, [2, 6, 7]],
    #               [6, [3, 8]],
    #               [7, [8, 10]],
    #               [8, [7]],
    #               [9, [7]],
    #               [10, [9, 11]],
    #               [11, [12]],
    #               [12, [10]]]

    test_graph = gc.create_kj_graph(test_graph)

    # print(str(test_graph))
    kosaraju(test_graph)
    print('Result:\n' + str(test_graph))
