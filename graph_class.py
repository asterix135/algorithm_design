class Vertex:
    """
    class to keep track of vertices in a graph and their associated edges
    """

    def __init__(self, key):
        """
        initialize vertex with id number and empty dictionary of edges
        """
        self._id = key
        self._connected_to = {}

    def add_neighbor(self, neighbor, weight=1):
        """
        add information about a connected vertex to the vertex's _connected_to
        dictionary
        key is vertex, value is weight
        """
        self._connected_to[neighbor] = weight

    def __str__(self):
        """
        returns human-readable version of vertex'e connections
        """
        return str(self._id) + ' connected to ' + str([node._id for node in
                                                       self._connected_to])

    def get_connections(self):
        """return list of connections"""
        return self._connected_to.keys()

    def get_id(self):
        """ returns id of vertex"""
        return self._id

    def get_weight(self, neighbor):
        """
        returns the weight of an edge betweeen self and a
        given neighbor
        """
        return self._connected_to[neighbor]


class Graph:
    """class to manage verices and edges in a graph"""

    def __init__(self):
        """
        contains a dictionary - _vertex_list - mapping vertex keys to vertex
        objects and a count of the number of vertices in the graph
        """
        self._vertex_list = {}
        self._vertex_count = 0

    def create_vertex(self, key):
        """
        creates a new vertex and returns that vertex
        """
        self._vertex_count += 1
        new_vertex = Vertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """ returns the vertex object associated with a key """
        if key in self._vertex_list:
            return self._vertex_list[key]
        else:
            return None

    def __contains__(self, key):
        """
        returns a boolean indicating whether a given vertex is in the graph
        """
        return key in self._vertex_list

    def add_edge(self, tail_key, head_key, weight=1):
        """
        adds a nee edge to thr graph. if either vertex is not present, it will
        be added first.
        edge is only added for the tail vertex
        """
        if tail_key not in self._vertex_list:
            self.create_vertex(tail_key)
        if head_key not in self._vertex_list:
            self.create_vertex(head_key)
        self._vertex_list[tail_key].add_neighbor(self._vertex_list[head_key],
                                                 weight)

    def get_vertices(self):
        """
        return a list of keys of all vertices in the graph
        """
        return self._vertex_list.keys()

    def __iter__(self):
        """returns an iterator of all vertices"""
        return iter(self._vertex_list.values())

    def remove_vertex(self, key):
        pass

    def remove_edge(self, tail_id, head_id, weight = 1):
        pass

    def get_edges(self):
        pass

    def get_edge_count(self):
        pass