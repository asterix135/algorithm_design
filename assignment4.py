import kosaraju
import collections


def read_in_graph():
    """
    reads in a text respresentation of a graph where each line consists
    of tail and head of an edge
    """
    problem_graph = kosaraju.gc.KjGraph('d')
    # filename = "SCC.txt"
    filename = "test_scc.txt"
    with open(filename) as file_in:
        for line in file_in:
            val = line.strip().split()
            tail, head = int(val[0]), int(val[1])
            problem_graph.add_edge(tail, head)
    return problem_graph


def top5_sccs(graph):
    """
    Finds top 5 SCCs by size in a graph that has been submitted to
    kosaraju's algorithm
    """
    scc_sizes = {}
    for node in graph:
        scc_id = node.get_leader()
        if scc_id in scc_sizes:
            scc_sizes[scc_id] += 1
        else:
            scc_sizes[scc_id] = 1
    sorted_scc_sizes = collections.OrderedDict(sorted(scc_sizes.items(),
                                                      key=lambda t: -t[1]))
    top5 = []
    for item in range(min(5, len(scc_sizes))):
        top5.append(sorted_scc_sizes.popitem(0))
    return top5


if __name__ == "__main__":
    print("starting read in")
    problem_graph = read_in_graph()
    print("finished read in")
    print()
    kosaraju.kosaraju(problem_graph)
    print(top5_sccs(problem_graph))
