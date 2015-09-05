"""
Kosaraju's Algorithm for finding Strongly Connected Components
"""

import graph_class_kosaraju as gc

# TODO: 1) Figure out how to have graph class keep track of sorts
# TODO: 2) Implement algorithm


def kosaraju(graph):
    rev_graph = graph.reverse_graph()
    time_value = 0
    start_value = None
    pass1_order = list(graph.get_vertices())
    pass1_order.sort(reverse=True)
    pass2_order = []

    def dfs(graph_dfs, node):
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

    def dfs_loop(graph_loop, order_list):
        nonlocal start_value
        for node in graph_loop:
            node.mark_unexplored()
        # TODO: This ordering won't work - need to fix
        for vertex_number in order_list:
            node = graph_loop.get_vertex(vertex_number)
            if not node.is_explored():
                start_value = node.get_node_id()
                dfs(graph_loop, start_value)
        return graph

    dfs_loop(rev_graph, pass1_order)
    print('rev_graph after dfs \n' + str(rev_graph))
    pass2_copy=pass2_order.copy()
    dfs_loop(graph, pass2_copy)






# basically 2 passes of DFS
#
# Given Graph G
#
# 1) Let G(rev) = G with all arcs reversed
# 2) Run DFS-Loop on G(rev) - n.b. you don't have to copy G into G(rev)
#      DFS-Loop means you have an outer loop where you look at each node in order
#      Goal: discover "magical ordering" of nodes for step 3
# 2a) Let f(v) = 'finishing time' of each Vertex
# 3) Run DFS-Loop on the original graph G
#      Goal: discover SCC's 1 by 1
#      Process nodes in decreasing order of finishing times
#      Label each node with a "leader"
#      SCCs are elements with the same 'leader'
#
#
# DFS-Loop(Graph G)
# global variable t=0 (# of nodes processed so far - gives us finishing times from 1st class)
# global variable S= Null (keeps track of most recent vertex from which DFS was called - leaders in 2nd pass)
#
# In 1st DFS, we go through in some arbitrary order
# In 2nd DFS we go through in order of decreasing finishing time
#
# For i = n down to 1
#      if i not yet explored
#           S = i
#           DFS (G, i)
#
# DFS(G, i)
#      - mark i as explored (for rest of DFS-Loop)
#      - set leader(i) = node S
#      - for each arc (i,j) in G:
#           if j not yet explored:
#                DFS (G, j)
#      - t += 1
#      - set f ( i ) = t  (f(i) is the finishing time for a node)
#
# Need to keep track of how you keep track of finishing times so you don't have to sort them



test_graph = [[1, [2]],
              [2, [3]],
              [3, [1, 4]],
              [4, [5]],
              [5, [6]],
              [6, [4]]]

test_graph = gc.create_kj_graph(test_graph)

# print(str(test_graph))
kosaraju(test_graph)
print('Result:\n' + str(test_graph))