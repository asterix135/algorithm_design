import undirected_graph as graph
import random

FILENAME = 'kargerMinCut.txt'

def mincut():
    """Implementation of mincut algorithm from class"""
    pass

def create_graph(filename):
    """create graph class object from file"""
    graph_data = open(filename, 'r')
    for line in graph_data:
        print(line.strip)
    graph_data.close()

if __name__ == '__main__':
    create_graph(FILENAME)
