"""
Kosaraju's Algorithm for finding Strongly Connected Components
"""

def kosaraju(graph):
    """
    runs kosaraju's algorithim on a directed graph to calculate
    strongly connected components
    takes graph as input and modifies that graph
    graph must be from kosaraju_graph_class
    """
    rev_graph = graph.reverse_graph()
    print("graph reversed")
    time_value = 0
    start_value = None
    pass1_order = list(graph.get_vertices())
    pass1_order.sort(reverse=True)
    print("pass 1 order calculated")
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
        while len(search_stack) > 0:
            active_node = search_stack.pop()
            active_node_id = active_node.get_node_id()
            if not active_node.is_explored():
                active_node.mark_explored()
                active_node.set_leader(start_value)
                search_stack.append(active_node)
                for edge in active_node.get_edges():
                    linked_vertex = graph_dfs.get_vertex(edge)
                    if not linked_vertex.is_explored():
                        search_stack.append(linked_vertex)
            elif active_node.get_finishing_time() == 0:
            # elif active_node_id not in pass2_order:
                time_value += 1
                active_node.set_finishing_time(time_value)
                pass2_order.insert(0, active_node_id)


    def dfs_loop(graph_loop, order_list):
        """main outer loop for algorithm"""
        nonlocal start_value
        for node in graph_loop:
            node.mark_unexplored()
            # node.set_finishing_time(0)
        for vertex_number in order_list:
            node = graph_loop.get_vertex(vertex_number)
            if not node.is_explored():
                # print(vertex_number)
                start_value = node.get_node_id()
                # dfs(graph_loop, start_value)
                dfs_non_recursive(graph_loop, start_value)
        return graph

    dfs_loop(rev_graph, pass1_order)
    print("pass 1 done")
    pass2_copy = pass2_order.copy()
    dfs_loop(graph, pass2_copy)
    print("pass 2 done")


