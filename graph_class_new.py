"""
Base graph class - impvoed
"""


class Vertex:
    """
    Vertex class for Graph
    """

    def __init__(self, vertex_id, edges=None):
        """
        Vertex takes two parameters - vertex_id and optional edges
        vertex_id is a number, vertex_id is a list
        """
        self._node_id = vertex_id

        if isinstance(edges, list):
            self._edge_list = edges
        else:
            self._edge_list = [edges] if edges is not None else []

    def __repr__(self):
        """printable list of nodes and edges for the object"""
        return "Node: " + str(self._node_id) + " Edge: " \
               + str(self._edge_list)

    def get_node_id(self):
        """returns vertex's node_kd"""
        return self._node_id

    def get_edges(self):
        """returns list of edges for current vertex"""
        return self._edge_list

    def add_edge(self, neighbor):
        """
        add connected vertex to the vertex's edge list
        """
        self._edge_list.append(neighbor)

    def remove_edge(self, neighbor):
        """
        remove one instance of neighbor information from edge list
        """
        while neighbor in self._edge_list:
            self._edge_list.remove(neighbor)


class Graph:
    """
    Basic graph class
    """

    def __init__(self, graph_type='u'):
        """
        No parameters needed - creates empty vertex dictionary
        by default initialized as undirected - set type to 'd' for directed
        """
        self._vertex_list = {}
        self._type = graph_type

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

    def __len__(self):
        """returns length of self._vertex_list"""
        return len(self._vertex_list)

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
        if type is u,neighbor info is added to both vertices' edge lists
        """
        if tail_key not in self._vertex_list.keys():
            self.create_vertex(tail_key)
        if head_key not in self._vertex_list.keys():
            self.create_vertex(head_key)
        self._vertex_list[tail_key].add_edge(self._vertex_list[head_key].get_node_id())
        if self._type == 'u':
            self._vertex_list[head_key].add_edge(
                self._vertex_list[tail_key].get_node_id())

    def get_vertices(self):
        """
        return a list of keys of all vertices in the graph
        """
        return self._vertex_list.keys()

    def get_vertex_count(self):
        """return number of vertices in graph"""
        return len(self._vertex_list)
