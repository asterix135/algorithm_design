"""
Graph and Vertex Classes for an Undirected, unweighted Graph
Allows Parallel edges
"""


class Vertex:
    """
    class to keep track of vertices in a graph and their associated edges
    """

    def __init__(self, key):
        """
        initialize vertex with id number and empty list of edges
        """
        self._id = key
        self._connected_to = []

    def __str__(self):
        """
        returns human-readable version of vertex's connections
        """
        return str(self._id) + ' connected to ' + str([node.get_id() for node
                                                       in self._connected_to])

    def add_neighbor(self, neighbor):
        """
        add connected vertex to the vertex's _connected_to
        """
        self._connected_to.append(neighbor)

    def remove_neighbor(self, neighbor):
        """
        remove one instance of neighbor information from _connected_to list
        """
        if neighbor in self._connected_to:
            self._connected_to.remove(neighbor)

    def get_connections(self):
        """return list of connections"""
        return self._connected_to

    def get_id(self):
        """ returns id of vertex"""
        return self._id


class Graph:
    """class to manage verices and edges in a directed graph"""

    def __init__(self):
        """
        creates a blank graph
        contains a dictionary - _vertex_list - mapping vertex keys to vertex
        objects and a count of the number of vertices in the graph
        edge list contains a single list of edges stored as (head, tail) tuples
            it's random whether a given vertex is head or tail
        """
        self._vertex_list = {}

    def __contains__(self, key):
        """
        returns a boolean indicating whether a given vertex is in the graph
        """
        return key in self._vertex_list

    def __iter__(self):
        """returns an iterator of all vertices"""
        return iter(self._vertex_list.values())

    def __str__(self):
        """returns human-readable list of nodes and neighbors"""
        output_string = "Vertex List:\n"
        for node in self._vertex_list:
            output_string += str(self.get_vertex(node)) + '\n'
        return output_string

    def create_vertex(self, key):
        """
        creates a new vertex and returns that vertex
        """
        new_vertex = Vertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """ returns the vertex object associated with a key """
        if key in self._vertex_list:
            return self._vertex_list[key]
        else:
            return None

    def add_edge(self, tail_key, head_key):
        """
        adds a new edge to the graph. If either vertex is not present, it will
        be added first.
        neighbor info is added to both vertices' _connected_to lists
        """
        if tail_key not in self._vertex_list:
            self.create_vertex(tail_key)
        if head_key not in self._vertex_list:
            self.create_vertex(head_key)
        self._vertex_list[tail_key].add_neighbor(self._vertex_list[head_key])
        self._vertex_list[head_key].add_neighbor(self._vertex_list[tail_key])

    def get_vertices(self):
        """
        return a list of keys of all vertices in the graph
        """
        return self._vertex_list.keys()

    def remove_vertex(self, key):
        """
        removes vertex from graph
        also removes all edges referencing the vertex
        """
        # 1. make sure vertex is in graph
        if key not in self._vertex_list:
            return None
        # 2. get list of connected vertices
        connected_nodes = self._vertex_list[key].get_connections()
        # 3. remove all relevant edges from connected vertices
        node_to_remove = self.get_vertex(key)
        for node in connected_nodes:
            while node_to_remove in node.get_connections():
                node.remove_neighbor(node_to_remove)
        # 4. update _edge_list
        delete_list = []
        for edge in self._edge_list:
            if edge[0] == node_to_remove or edge[1] == node_to_remove:
                delete_list.append(edge)
        for edge_to_delete in delete_list:
            self._edge_list.remove(edge_to_delete)
        # 4. remove actual vertex
        self._vertex_list.pop(key)
        # 5. update vertex count

    def remove_edge(self, tail, head):
        """
        removes one edge from a graph
        takes two vertices (NOT IDs) as an argument
        for each vertex, removes reference to other vertex
        removes edge from graph's edge list
        """
        tail.remove_neighbor(head)
        head.remove_neighbor(tail)
        # should probably break out as separate function
        if [head, tail] in self._edge_list:
            self._edge_list.remove([head, tail])
        else:
            self._edge_list.remove([tail, head])

    def get_edges(self):
        """
        returns a list of edges in the graph
        edges represented as a tuple: (tail, head)
        """
        return self._edge_list

    def get_edge_count(self):
        """return number of edges in graph"""
        return len(self.get_edges())

    def get_vertex_count(self):
        """return number of vertices in graph"""
        return len(self._vertex_list)

    def fuse_vertices(self, tail, head):
        """
        takes two vertices (NOT indexes) as arguments
        fuses two vertices (head and tail)
        deletes one edge between the two
        adds head's neighbor list to tail
        updates edge_list to replace all head references with tail
        removes self-referential edges
        """
        # Make sure the vertices have an edge between them and delete that edge
        # if [tail, head] in self._edge_list:
        #     self.remove_edge(tail, head)
        # elif [head, tail] in self._edge_list:
        #     self.remove_edge(head, tail)
        # else:
        #     return None
        while [tail, head] in self._edge_list:
            self.remove_edge(tail, head)
        while [head, tail] in self._edge_list:
            self.remove_edge(head, tail)



        # go through head neighbors
        # for each - append neighbor to head unless it'd be self-referential
        # also update neighbor list for each neighbor to refer to tail

        for neighbor in head.get_connections():
            if neighbor != tail:
                tail.add_neighbor(neighbor)
                neighbor.remove_neighbor(head)
                neighbor.add_neighbor(tail)

        # update edge_list by replacing head with tail in all edges
        # and deleting resulting self-referenes
        iterator_list = list(self._edge_list)
        for edge in iterator_list:
            if edge[0] == head:
                if edge[1] == tail:
                    self._edge_list.remove(edge)
                else:
                    edge[0] = tail
            elif edge[1] == head:
                edge[1] = tail
        self._vertex_list.pop(head.get_id())

    def copy_graph(self):
        new_graph = Graph()
        for edge in self._edge_list:
            new_graph.add_edge(edge[0].get_id(), edge[1].get_id())
        return new_graph
