"""
implementation of Karger's minimum cut algorithm
"""

import random
import copy


FILENAME = 'kargerMinCut.txt'
# FILENAME = 'test_graph.txt'


class Adjacency:
    """
    Class to keep track of nodes and edges in a graph
    The graph itself should be a list of these objects
    Class is mainly designed to be used in a contraction algorithm
    """

    def __init__(self, node, edge):
        """
        Initiate the object with a list of nodes and a list of edges"""
        self._node_list = node
        self._edge_list = edge

    def __repr__(self):
        """printable list of nodes and edges for the object"""
        return "Node: " + str(self._node_list) + " Edge: " \
               + str(self._edge_list)

    def get_nodes(self):
        """returns list of nodes included in current object"""
        return self._node_list

    def get_edges(self):
        """returns list of edges included in current object"""
        return self._edge_list

    def merge_nodes(self, other_adjacency):
        """
        merges another node with this one
        keeps track of nodes merged
        eliminates self-referential edges
        """
        self._node_list += other_adjacency.get_nodes()
        new_edge_list = []
        for merge_edge in other_adjacency.get_edges() + self._edge_list:
            if merge_edge not in self._node_list:
                new_edge_list.append(merge_edge)
        self._edge_list = new_edge_list


def cut(graph, seed=None):
    """
    recursive algorithm that returns two fused nodes (Adjacency objects)
    showing best calculated cut
    """
    if len(graph) == 2:
        return graph
    else:
        random.seed(seed)
        random_adjacency = random.choice(graph)
        merge_target = random.choice(random_adjacency.get_edges())
        for adj in graph:
            if merge_target in adj.get_nodes():
                merge_partner = adj
                break
        random_adjacency.merge_nodes(merge_partner)
        graph.remove(merge_partner)
        return cut(graph, seed)


def mincut(graph):
    """
    Runs the random contraction algorithm n**2 times providing
    a probability of failure of 1/n
    """
    best_cut = float('inf')
    for trial in range(len(graph)**2):
        trial_graph = copy.deepcopy(graph)
        trial_cut = len(cut(trial_graph)[0].get_edges())
        if trial_cut < best_cut:
            best_cut = trial_cut
            cut_graph = trial_graph
        if trial % 500 == 0:
            print('trial # ' + str(trial) + ' best cut = ' + str(best_cut))
    return best_cut, cut_graph


def create_graph(filename):
    """
    create graph class object from file
    assumes no parallel edges in originating graph file
    """
    graph_source = open(filename, 'r')
    graph_data = [[[int(line.split()[0])], [int(i) for i in line.split()[1:]]]
                  for line in graph_source]
    graph = [Adjacency(node[0], node[1]) for node in graph_data]
    graph_source.close()
    return graph


def class_problem():
    best_cut = mincut(create_graph(FILENAME))
    return best_cut[0]


if __name__ == '__main__':
    answer = class_problem()
    print('Answer = ' + str(answer))
