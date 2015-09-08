import kosaraju
# import sys
# import resource


# sys.setrecursionlimit(10**6)
# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


def read_in_graph():
    problem_graph = kosaraju.gc.KjGraph('d')
    with open("SCC.txt") as file_in:
        for line in file_in:
            val = line.strip().split()
            tail, head = int(val[0]), int(val[1])
            problem_graph.add_edge(tail, head)
    return problem_graph


if __name__ == "__main__":
    print("starting read in")
    problem_graph = read_in_graph()
    print("finished read in")
    print()
    kosaraju.kosaraju(problem_graph)
