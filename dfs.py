"""Recursive DFS graph search"""

# Graph structure for DFS is the same as BFS
import bfs

def dfs(graph, start_node=1):
    """
    Takes graph & start vertex as parameters
    explores graph with DFS approach
    """
    start_vertex = graph.get_vertex(start_node)
    if not start_vertex.get_nodes()[0][1]:
        start_vertex.mark_explored()
    for edge in start_vertex.get_edges():
        linked_vertex = graph.get_vertex(edge)
        if not linked_vertex.get_nodes()[0][1]:
            dfs(graph, edge)

if __name__ == '__main__':
    test_graph = bfs.create_graph(bfs.test_graph_data)
    print(str(test_graph))
    print('run dfs')
    dfs(test_graph, 1)
    print(str(test_graph))
