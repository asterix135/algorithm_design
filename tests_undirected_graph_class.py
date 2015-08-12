"""test battery for undirected graph class"""

import undirected_graph as graph
import random


def test():
    g = graph.Graph()
    g.create_vertex(1)
    g.create_vertex(2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    print(str(g.get_vertex(1)))
    print(str(g.get_vertex(2)))
    print(str(g.get_vertex(3)))
    print(str(g.get_vertex(4)))
    print()

    g.remove_vertex(4)
    print(str(g.get_vertex(1)))
    print(str(g.get_vertex(2)))
    print(str(g.get_vertex(4)))
    print()

    print(g.get_edges())
    print(g.get_edge_count())
    print()

    print('remove edge')
    g.remove_edge(g.get_vertex(1), g.get_vertex(2))
    print(g.get_edge_count())
    print(str(g.get_vertex(1)))
    print(str(g.get_vertex(2)))
    print(str(g.get_vertex(3)))
    print()

    print('test str for graph')
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    print(str(g))
    print("edges")
    print(g.get_edge_count())
    print('vertices')
    print(g.get_vertex_count())
    print()

    print('test fuse')
    tail = g.get_vertex(1)
    head = g.get_vertex(4)
    g.fuse_vertices(tail, head)
    print(str(g))
    print("edges")
    print(g.get_edge_count())
    print('vertices')
    print(g.get_vertex_count())
    print()

    print('test fuse using an edge')
    fuse_edge = random.choice(g.get_edges())
    g.fuse_vertices(fuse_edge[0], fuse_edge[1])
    print(str(g))
    print("edges")
    print(g.get_edge_count())
    print('vertices')
    print(g.get_vertex_count())
    print()
    print('tests complete')


if __name__ == '__main__':
    test()
