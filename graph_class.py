"""
Base graph class
"""


class Vertex:
    """
    Vertex class for Graph
    """

    def __init__(self, vertex_id, edges=None):
        """
        Vertex takes two parameters - vertex_id and optional edges
        both are lists
        """
        if isinstance(vertex_id, list):
            self._node_id = vertex_id
        else:
            self._id = [vertex_id]

        if isinstance(edges, list):
            self._edge_list = edges
        else:
            self._edge_list = [edges] if edges is not None else []

    def __repr__(self):
        """printable list of nodes and edges for the object"""
        return "Node: " + str(self._node_id) + " Edge: " \
               + str(self._edge_list)

    def get_nodes(self):
        """returns list of node ids included in current object"""
        return self._node_id

    def get_edges(self):
        """returns list of edges included in current object"""
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

    def merge_nodes(self, other_vertex):
        """
        merges another node with this one
        keeps track of nodes merged
        eliminates self-referential edges
        """
        self._node_id += other_vertex.get_nodes()
        new_edge_list = []
        for merge_edge in other_vertex.get_edges() + self._edge_list:
            if merge_edge not in self._node_id:
                new_edge_list.append(merge_edge)
        self._edge_list = new_edge_list


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
        if tail_key not in self._vertex_list:
            self.create_vertex(tail_key)
        if head_key not in self._vertex_list:
            self.create_vertex(head_key)
        self._vertex_list[tail_key].add_neighbor(self._vertex_list[head_key])
        if self._type == 'u':
            self._vertex_list[head_key].add_neighbor(
                self._vertex_list[tail_key])

    def get_vertices(self):
        """
        return a list of keys of all vertices in the graph
        """
        return self._vertex_list.keys()

    def get_vertex_count(self):
        """return number of vertices in graph"""
        return len(self._vertex_list)
