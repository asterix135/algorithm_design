import undirected_graph as graph
import random

FILENAME = 'kargerMinCut.txt'
# FILENAME = 'test_graph.txt'

def mincut(graph):
    """Implementation of mincut algorithm from class"""
    best_cut = float('inf')
    for trial in range(graph.get_vertex_count() ** 2):
        trial_graph = graph.copy_graph()

        # print('trial graph for trial #:' + str(trial))
        # print(str(trial_graph) + '\n')

        for node in range(graph.get_vertex_count() - 2):
            random.seed(trial)
            fusion_edge = random.choice(trial_graph.get_edges())

            # print('fusion edge')
            # print(str(fusion_edge[0].get_id()) + ', ' +
            #       str(fusion_edge[1].get_id()))

            trial_graph.fuse_vertices(fusion_edge[0], fusion_edge[1])

            # print('one iteration of fuse')
            # print(str(trial_graph) + '\n')

        trial_cut = trial_graph.get_edge_count()
        print('trial cut = ' + str(trial_cut))
        if trial_cut < best_cut:
            best_cut = trial_cut
    return best_cut


def create_graph(filename):
    """
    create graph class object from file
    assumes no parallel edges in originating graph file
    """
    new_graph = graph.Graph()
    graph_data = open(filename, 'r')

    edge_count = 0

    for line in graph_data:
        node_data = line.strip().split('\t')
        for neighbor in range(1, len(node_data)):
            check_edge = [new_graph.get_vertex(int(node_data[neighbor])),
                          new_graph.get_vertex(int(node_data[0]))]
            if check_edge not in new_graph.get_edges():
                new_graph.add_edge(int(node_data[0]), int(node_data[neighbor]))

                edge_count += 1
    graph_data.close()

    # print(str(new_graph))
    # print('vertices: ' + str(new_graph.get_vertex_count()))
    # print('edges: ' + str(new_graph.get_edge_count()))
    # print('edge_count: ' + str(edge_count))
    #
    return new_graph


def run_class_problem():
    problem_graph = create_graph(FILENAME)
    best_cut = mincut(problem_graph)
    return best_cut

if __name__ == '__main__':
    answer = run_class_problem()
    print('min cut = ' + str(answer))
