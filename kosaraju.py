"""
Kosaraju's Algorithm for finding Strongly Connected Components
"""

import graph_class_kosaraju as gc

# TODO: 1) Figure out how to have graph class keep track of sorts
# TODO: 2) Implement algorithm


def kosaraju(graph):
    rev_graph = graph.reverse_graph()
    time_value = 0
    start_vertex = None
    pass2_order = []

    def dfs(graph, node):
        # TODO: implement dfs
        nonlocal time_value, start_vertex
        start_vertex = graph.vertex(node)


    def dfs_loop(graph):
        # TODO: implment dfs_loop
        for node in graph:
            node.mark_unexplored()
        # TODO: This ordering won't work - need to fix
        for node in graph:
            if not node.is_explored():
                dfs(rev_graph, node.get_node_id())
        return graph




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
