"""
Topological Sort implementation
"""

import dfs



# DFS - Loop (graph G)
# - mark all nodes unexplored
# - current_label = n (count down as explored - to keep track of ordering)
# - for each vertex v in G
#          - if v not yet explored in some prevous DFS call
#                DFS - (G, v)
#                     at end of DFS (NOT DFS -loop) - when there is nowhere else to go
#                          set f(s) = current value
#                          current_value -= 1