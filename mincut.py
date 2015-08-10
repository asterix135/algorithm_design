import undirected_graph as graph
import random
import copy

FILENAME = 'kargerMinCut.txt'

def mincut(graph):
    """Implementation of mincut algorithm from class"""
    best_cut = float('inf')
    for trial in range(graph.get_vertex_count() ^ 2):
        trial_graph = copy.deepcopy(graph)
        for node in range(graph.get_vertex_count() - 2):
            random.seed(trial)
            fusion_edge = random.sample(trial_graph.get_edges(), 1)
            trial_graph.fuse_vertices(fusion_edge[0], fusion_edge[1])
        trial_cut = trial_graph.get_edge_count()
        if trial_cut < best_cut:
            best_cut = trial_cut
    return best_cut


def create_graph(filename):
    """create graph class object from file"""
    new_graph = graph.Graph()
    graph_data = open(filename, 'r')
    for line in graph_data:
        node_data = line.strip().split('\t')
        for neighbor in range(1, len(node_data)):
            new_graph.add_edge(node_data[0], node_data[neighbor])
    graph_data.close()
    return new_graph


def run_class_problem():
    problem_graph = create_graph(FILENAME)
    answer = mincut(problem_graph)
    return answer
    # best_cut = float('inf')
    # for trial in range(problem_graph.get_vertex_count() ^ 2):
    #     problem_graph = create_graph(FILENAME)
    #     random.seed(trial)
    #     cut_trial = mincut(problem_graph)
    #     if cut_trial < best_cut:
    #         best_cut = cut_trial
    # return best_cut

if __name__ == '__main__':
    answer = run_class_problem()
    print(answer)

